from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import (
    UpdateView,
    DeleteView,
    ListView,
    CreateView,
    DetailView
)
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Status
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = [
        "title", "subtitle", "body",
        "author",
    ]

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list") #we dont have url patterns yet so list isn't a url pattern yet

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    
class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'  # Your template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        published = Status.objects.get(name="published")
        context["posts"] = (
            Post.objects
            .filter(status=published)
            .order_by("created_on").reverse()
        )
        return context
    
class DraftPostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft = Status.objects.get(name="draft")
        context["posts"] = (
            Post.objects
            .filter(status=draft)
            .filter(author=self.request.user)
            .order_by("created_on").reverse()
        )
        return context
    

class ArchivedPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        archived = Status.objects.get(name="archived")
        context["posts"] = (
            Post.objects.filter(status=archived)
            .order_by("created_on").reverse()
        )
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new_post.html"
    model = Post
    fields = [
        "title", "subtitle", "body", "author", "status"
    ]
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Create your views here.
