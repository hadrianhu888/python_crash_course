"""Defines URL patterns for hte leraning_logs and"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path ('', views.index, name='index'),
    path('', views.index, name = 'index'),
    # page that shows all topics
    path('topics/', views.topics, name = 'topics'),
    # Detail page for a single topic
    path('topics/<int.topic_id>/', views.Topic, name = 'topic'),
]