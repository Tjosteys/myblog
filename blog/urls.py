from django.urls import path
from . import views

urlpatterns = [
	path('', views.BlogListView.as_view(), name='post_list'),
	path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
	path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
	path('post/edit/<int:pk>/', views.BlogUpdateView.as_view(), name='post_edit'),
	path('post/delete/<int:pk>/', views.BlogDeleteView.as_view(), name='post_delete'),
]