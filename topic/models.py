from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings
# Create your models here.

class Topic(models.Model):
	author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	title = models.CharField(max_length=200) 
	text = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	#published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('topic_page',args=[str(self.id)])

class Comments(models.Model):
	"""docstring for ClassName"""
	topic=models.ForeignKey('Topic',on_delete=models.CASCADE)
	published_date = models.DateTimeField(default=timezone.now)
	comment=models.TextField(blank=True,null=True)
	author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	#author=models.CharField(max_length=50,blank=True,default="anonymous")
	

	def __str__(self):
		return str(self.published_date)+" "+self.author

	def get_absolute_url(self):
		return reverse('topic_page')