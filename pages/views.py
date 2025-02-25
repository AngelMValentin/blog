from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class PostsPageView(TemplateView):
    template_name = 'pages/posts.html'

class CreatePageView(TemplateView):
    template_name = 'posts/new_post.html'

# Create your views here.
