from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Topic, Comments
from .forms import TopicForm, CommentForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls  import reverse_lazy
from django.views.generic.edit import DeleteView,UpdateView,CreateView
from django.views.generic import ListView

#from django.contrib.auth.forms import UserCreationForm

#def topic_list(request):
#	topics = Topic.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#	return render(request, 'topic/topic_list.html', {'topics':topics})

class topic_list(ListView):
	model = Topic
	template_name = 'topic_list.html'

def topic_page(request, pk):
	topic = get_object_or_404(Topic, pk = pk)
	comment_list= Comments.objects.filter(topic=topic)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.topic = topic
			comment.author = request.user
			comment.published_date = timezone.now()
			comment.save()
			#return redirect('post_detail', pk=post.pk)
	else:
		form = CommentForm()
	#return render(request, 'post_edit.html', {'form': form})
	return render(request, 'topic/topic_page.html', {'topic': topic, 'comment_list' : comment_list, 'form': form})

#def topic_new(request):
#	if request.method == "POST":
#		form = TopicForm(request.POST)
#		if form.is_valid():
#			topic = form.save(commit=False)
#			topic.author = request.user
#			topic.published_date = timezone.now()
#			topic.save()
#			return redirect('topic_page', pk=topic.pk)
#	else:
#		form = TopicForm()
#	return render(request, 'topic/topic_new.html', {'form': form})

class topic_new(LoginRequiredMixin, CreateView):
	model = Topic
	template_name = 'topic_new.html'
	fields = ('title','text','date')
	login_url = 'login'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class topic_edit(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
	model = Topic
	template_name = 'topic_edit.html'
	fields = ('title', 'text', 'date')
	login_url = 'login'

	def test_func(self):
		obj = super(topic_delete, self).get_object()
		if obj.author == self.request.user:
			return obj.author == self.request.user
		else:
			raise Http404

class topic_delete(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
	model = Topic
	template_name = 'topic_delete.html'	
	success_url = reverse_lazy('topic_list')
	login_url = 'login'

	def test_func(self):
		obj = super(topic_delete, self).get_object()
		if obj.author == self.request.user:
			return obj.author == self.request.user
		else:
			raise Http404
		


#def signup(request):
#	if request.method == 'POST':
#		form = SignUpForm(request.POST)
#		if form.is_valid():
#			form.save()
#			username = form.cleaned_data.get('username')
#			raw_password = form.cleaned_data.get('password1')
#			user = authenticate(username=username, password=raw_password)
#			login(request, user)
#			return redirect('/')
#	else:
#		form = SignUpForm()
#	return render(request, 'signup.html', {'form': form})

#def topic_edit(request, pk):
#	topic = get_object_or_404(Topic, pk=pk)
#	if request.method == "POST":
#		form = TopicForm(request.POST, instance=topic)
#		if form.is_valid():
#			topic = form.save(commit=False)
#			topic.author = request.user
#			topic.published_date = timezone.now()
#			topic.save()
#			return redirect('topic_page', pk=topic.pk)
#	else:
#		form = TopicForm(instance=topic)
#	return render(request, 'topic/topic_edit.html', {'form': form})