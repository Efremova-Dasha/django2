from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from django.views.generic import TemplateView
from django.urls import reverse_lazy
from datetime import datetime
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required

from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .filters import PostFilter
from .forms import PostForm
from .models import Post
from .models import Category

from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.utils.translation import gettext as _
from django.http import HttpResponse

@cache_page(100)
def home(request):
    return render(request, 'home.html')

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


class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'post_edit.html'


class ProtectedView(LoginRequiredMixin, TemplateView):
    template_name = 'post_delete.html'


class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.types = 'NEWS'
        return super().form_valid(form)


class ArticlesCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.types = 'ARTI'
        return super().form_valid(form)


class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.types = 'NEWS'
        return super().form_valid(form)


class ArticlesUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.types = 'ARTI'
        return super().form_valid(form)


class NewsDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class CategoryListView(ListView):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('-time_date')
        return queryset

    def qet_context_data(self, **kwargs):
        context = super().qet_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались'
    return render(request, 'subscribe.html', {'category':category, 'message':message})

@login_required
def unsubscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.remove(user)
    return redirect(f'/news/categories/{category.pk}')


class AuthorsListView(ListView):
    model = Post
    template_name = 'authors_list.html'
    context_object_name = 'authors_post_list'
    paginate_by = 10

    def get_queryset(self):
        self.author = get_object_or_404(self.author, id=self.kwargs['pk'])
        queryset = Post.objects.filter(author=self.author).order_by('-date_creation')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.author
        return context


class PostTypeListView(ListView):
    model = Post
    template_name = 'post_type.html'
    context_object_name = 'post_type_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.filter(post_type=self.get_type()[0]).order_by('-date_creation')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_type'] = self.get_type()[1]
        return context

    def get_type(self):
        path_type = self.request.META['PATH_INFO']
        if path_type == '/news/type/news':
            return 'news', 'новостей'
        elif path_type == '/news/type/article':
            return 'article', 'статей'


class Index(View):
    def get(self, request):
        string = _('Hello world')

        context = {
            'string': string
        }

        return HttpResponse(render(request, 'Index.html', context))