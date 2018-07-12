from . import views
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
	path('', views.topic_list, name='topic_list'),
	path('topic/<int:pk>/', views.topic_page, name='topic_page'),
	path('topic/new/', views.topic_new, name='topic_new'),
	path('post/<int:pk>/edit/', views.topic_edit, name='topic_edit'),
	path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('admin/', admin.site.urls)
	]