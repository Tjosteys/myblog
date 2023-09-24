from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
	title = models.CharField(max_length=200)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title