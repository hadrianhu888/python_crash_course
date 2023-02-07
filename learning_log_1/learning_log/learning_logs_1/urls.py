"""Defines URL patterns for learning_logs_1."""

from django.urls import path
from . import views

app_name = "learning_logs_1"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Page that shows all topics
    path("topics/", views.topics, name="topics"),
]