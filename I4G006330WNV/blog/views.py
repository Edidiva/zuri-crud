#from django.shortcuts import render
from .models import Post
from django.views import generic
from django.urls import reverse_lazy
# from django.views.generic import CreateView
# from django.views.generic import DetailView
# from django.views.generic import UpdateView
# from django.views.generic import ListView
# from django.views.generic import DeleteView


# Create your views here.

class PostListView(generic.ListView):
    model= Post


class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")


class PostDetailView(generic.DetailView):
    model=Post


class PostUpdateView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url  = reverse_lazy("blog:all")

 

    
