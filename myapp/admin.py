from django.contrib import admin
from .models import *

# Register your models here.
class PostFormAdmin(admin.ModelAdmin):
    list_display = ['title','published', 'slug']
    ordering = ['-published',]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostFormAdmin)