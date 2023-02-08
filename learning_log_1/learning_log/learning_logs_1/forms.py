""""This is the forms module for the learning_logs app."""

from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """This is the form for adding a new topic."""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
class EntryForm(forms.ModelForm):
    """This is the form for adding a new entry."""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        
