from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
class BlogListView(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'blog/bloglist.html'


class BlogDetailView(DetailView):
	model = Post
	template_name = 'blog/blogdetail.html'