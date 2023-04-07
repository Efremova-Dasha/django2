from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.template.loader import render_to_string

from NewsPaper.news.models import PostCategory


def send_notifications(preview, pk, title, subscribers):
    from NewsPaper.NewsPaper import settings
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/post/{pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


#@receiver(m2m_changed, sender=PostCategory)
@shared_task(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instanse, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instanse.category.all()
        subscribers: list[str] = []

        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]

        send_notifications(instanse.preview(), instanse.pk, instanse.title, subscribers)