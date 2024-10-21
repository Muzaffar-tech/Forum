from django.contrib import admin
from .models import Topic, Reply, Comment

# Register your models here.

admin.site.register(Topic)
admin.site.register(Reply)
admin.site.register(Comment)
