from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Topic
from .forms import TopicForm

def topic_list(request):
	topics = Topic.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'topic/topic_list.html', {'topics':topics})

def topic_page(request, pk):
	topic = get_object_or_404(Topic, pk = pk)
	return render(request, 'topic/topic_page.html', {'topic': topic})

def topic_new(request):
	if request.method == "POST":
		form = TopicForm(request.POST)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.author = request.user
			topic.published_date = timezone.now()
			topic.save()
			return redirect('topic_page', pk=topic.pk)
	else:
		form = TopicForm()
	return render(request, 'topic/topic_edit.html', {'form': form})

def topic_edit(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.method == "POST":
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.published_date = timezone.now()
            topic.save()
            return redirect('topic_detail', pk=topic.pk)
    else:
        form = TopicForm(instance=topic)
    return render(request, 'topic/topic_edit.html', {'form': form})