from . import views
from django.urls import path

urlpatterns = [
	path('', views.topic_list, name='topic_list'),
	]