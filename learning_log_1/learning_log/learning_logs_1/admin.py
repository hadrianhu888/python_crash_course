from django.contrib import admin
from .models import Topic, Entry
# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.site_header = "Learning Log Administration"
admin.site.site_title = "Learning Log Admin Portal"
admin.site.index_title = "Welcome to Learning Log Admin Portal"
admin.site.site_url = "http://127.0.0.8000"
