from django import forms
from .models import Topic, Comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TopicForm(forms.ModelForm):
	"""docstring for TopicForm"""
	class Meta:
		model = Topic
		fields = ('author', 'title','text')
		

class CommentForm(forms.ModelForm):
	"""docstring for CommentForm"""
	class Meta:
		model=Comments
		fields=('comment',)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
