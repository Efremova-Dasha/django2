from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):

    model = Post
    ordering = 'title'
    template_name = 'flatpages/posty.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context


class PostDetail(DetailView):

    model = Post
    template_name = 'flatpages/posto.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context