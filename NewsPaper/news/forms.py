from django import forms
from django.core.exceptions import ValidationError
from django_filters import DateFilter

from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(min_length=4)


    class Meta:
        model = Post
        fields = [
            'title',
            'types',
            'content',
            'category',
            'author'
        ]

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get("content")
        title = cleaned_data.get("title")

        if title == content:
            raise ValidationError(
                "Содержание не должно быть идентично заголовку."
            )

        return cleaned_data
