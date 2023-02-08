"""Defines URL patterns for learning_logs_1."""

from django.urls import path
from . import views

app_name = "learning_logs_1"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Page that shows all topics
    path("topics/", views.topics, name="topics"),
    # page for adding new topic
    path("new_topic/", views.new_topic, name="new_topic"),
    # Page for adding a new entry
    path ("new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),
    # Page for editting an entry
    path ("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
]