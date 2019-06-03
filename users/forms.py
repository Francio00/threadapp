from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	"""docstring for CustomUserCreationForm"""
	class Meta(UserCreationForm):
		"""docstring for Meta"""
		model = CustomUser
		fields = ('username','email','age',)

class CustomUserChangeFrom(UserChangeForm):
	"""docstring for CustomUserChangeFrom"""
	class Meta:
		model = CustomUser
		fields = ('username','email','age',)
		
			
