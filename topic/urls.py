from . import views
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views as topic_views
urlpatterns = [
	path('', views.topic_list.as_view(), name='topic_list'),	#lista topic
	path('topic/new/', views.topic_new, name='topic_new'),	#nuovo topic
	path('topic/<int:pk>/', views.topic_page, name='topic_page'),	#dettagli di un topic
	path('topic/<int:pk>/edit/', views.topic_edit.as_view(), name='topic_edit'),	#modifica topic
	path('topic/<int:pk>/delete/', views.topic_delete.as_view(), name='topic_delete'), #cancellazione topic
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('users/',include('django.contrib.auth.urls')),
    path('',TemplateView.as_view(template_name='home.html'), name='home')
    #path('login/', auth_views.login, name='login'),
	#path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    #path('signup/', topic_views.signup, name='signup'),
	]