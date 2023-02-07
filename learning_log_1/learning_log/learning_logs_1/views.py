from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    """The home page for Learning Log"""
    return render(request, "learning_logs_1/index.html")

def topics(request):
    """Show all topics."""
    topics = models.Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_logs_1/topics.html", context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = models.Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs_1/topic.html", context)

