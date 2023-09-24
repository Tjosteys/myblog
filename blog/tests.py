from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.
class BlogTest(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user(username='testuser', email='test@gmail.com', password='secret')

		self.post = Post.objects.create(title='a good title', body='Nice body content', author=self.user,)


	def test_string_representation(self):
		post = Post(title='a good title')
		self.assertEqual(str(post), post.title)

	def test_post_content(self):
		self.assertEqual(f'{self.post.title}', 'a good title')
		self.assertEqual(f'{self.post.author}', 'testuser')
		self.assertEqual(f'{self.post.body}', 'Nice body content')

	def tetst_post_list_view(self):
		response = self.client.get(reverse('bloglist'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Nice body content')
		self.assertTemplateUsed(response, 'blog/bloglist.html')

	def test_post_detail_view(self):
		response = self.client.get('/blog/post/1/')
		no_response = self.client.get('/blog/post/100000/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(no_response.status_code, 404)
		self.assertContains(response, 'a good title')
		self.assertTemplateUsed(response, 'blog/blogdetail.html')