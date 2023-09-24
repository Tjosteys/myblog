from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class BlogListView(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'blog/post_list.html'


class BlogDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'


class BlogCreateView(CreateView):
	model = Post
	template_name = 'blog/post_new.html'
	fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
	model = Post
	template_name = 'blog/post_edit.html'
	fields = ['title', 'body']

class BlogDeleteView(DeleteView):
	model = Post
	template_name = 'blog/post_delete.html'
	success_url = reverse_lazy('post_list')