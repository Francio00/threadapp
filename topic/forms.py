from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
	"""docstring for TopicForm"""
	class Meta:
		model = Topic
		fields = ('author', 'title','text')
		