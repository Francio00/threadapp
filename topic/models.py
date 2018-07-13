from django.db import models
from django.utils import timezone
# Create your models here.

class Topic(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Comments(models.Model):
	"""docstring for ClassName"""
	topic=models.ForeignKey('Topic',on_delete=models.CASCADE)
	published_date = models.DateTimeField(default=timezone.now)
	comment=models.TextField(blank=True,null=True)
	author=models.CharField(max_length=50,blank=True,default="anonymous")

	def __str__(self):
		return str(self.published_date)+" "+self.author