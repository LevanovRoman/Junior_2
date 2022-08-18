
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import *

menu_old = ['Home', 'About', 'Portfolio', 'Contact', 'Blog']
menu = [{'title': 'Home', 'url_name': 'home'},
        {'title': 'About', 'url_name': 'about'},
        {'title': 'Portfolio', 'url_name': 'portfolio'},
        {'title': 'Contact', 'url_name': 'contact'},
        {'title': 'Blog', 'url_name': 'blog'},
        {'title': 'Add post', 'url_name': 'add_post'},
         ]

def index(request):
    context = {'menu': menu_old, 'title': "Блог"}
    return render(request, 'juniorapp/index.html', context=context)

# def blog(request):
#     posts = Blog.objects.all()
#     context = {'posts': posts, 'menu': menu, 'title': "Блог"}
#     return render(request, 'juniorapp/blog.html', context=context)
class BlogHome(ListView):
    model = Blog
    template_name = 'juniorapp/blog.html'
    context_object_name = 'posts'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = "Блог"
        return context
    def get_queryset(self):
        return Blog.objects.filter(is_published=True)

def about(request):
    return render(request, 'juniorapp/about.html')

def contact(request):
    return render(request, 'juniorapp/contact.html', {'title': 'Контакты'})

def login(request):
    return render(request, 'juniorapp/login.html', {'title': 'login'})

def portfolio(request):
    return render(request, 'juniorapp/portfolio.html', {'title': 'Портфолио'})

# def show_post(request, post_slug):
#     post = get_object_or_404(Blog, slug=post_slug)
#     context = {"post": post, "menu": menu, "title": post.title, "cat_selected": post.cat_id}
#     return render(request, 'juniorapp/post.html', context=context)
class ShowPost(DetailView):
    model = Blog
    template_name = 'juniorapp/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post'].title
        return context


# def add_post(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     context = {'form': form, 'menu': menu, 'title': "Добавить пост"}
#     return render(request, 'juniorapp/add_post.html', context=context)
class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'juniorapp/add_post.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление поста'
        return context

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'juniorapp/register.html'
    success_url = reverse_lazy('login')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Регистрация'
        return context
