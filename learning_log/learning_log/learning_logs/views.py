from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

def topics(request, topic_id):
    """Show all topics in the learning log"""
    topics = Topic.objects.order_by('date_added')
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topics, 'entries': entries}
    return render(request, 'learning_logs/topics.html', context)

