from django.urls import reverse_lazy
from datetime import datetime

from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .filters import PostFilter
from .forms import PostForm
from .models import Post


class PostList(ListView):

    model = Post
    ordering = 'title'
    template_name = 'flatpages/posty.html'
    context_object_name = 'post'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_new'] = None
        context['filterset'] = self.filterset
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


class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.article_or_news = 'NEWS'
        return super().form_valid(form)


class ArticlesCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.article_or_news = Post.news
        return super().form_valid(form)


class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    queryset = Post.objects.filter(types='NEWS')
    template_name = 'post_edit.html'


class ArticlesUpdate(UpdateView):
    form_class = PostForm
    model = Post
    queryset = Post.objects.filter(types='ARTI')
    template_name = 'post_edit.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news_list')
    queryset = Post.objects.filter(types='NEWS')


class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news_list')
    queryset = Post.objects.filter(types='ARTI')
