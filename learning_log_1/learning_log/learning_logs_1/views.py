from django.shortcuts import render
from . import models
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from .forms import Topic
from django.http import Http404

# Create your views here.


def index(request):
    """The home page for Learning Log"""
    return render(request, "learning_logs_1/index.html")


@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404
    context = {"topics": topics}
    return render(request, "learning_logs_1/topics.html", context)


@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = models.Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs_1/topic.html", context)


@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            form.save()
            return HttpResponseRedirect(reverse("learning_logs_1:topics"))
    context = {"form": form}
    return render(request, "learning_logs_1/new_topic.html", context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = models.Topic.objects.get(id=topic_id)
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse("learning_logs_1:topic", args=[topic_id]))
    context = {"topic": topic, "form": form}
    return render(request, "learning_logs_1/new_entry.html", context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = models.Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != "POST":
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("learning_logs_1:topic", args=[topic.id]))
    context = {"entry": entry, "topic": topic, "form": form}
    return render(request, "learning_logs_1/edit_entry.html", context)
