from csv import list_dialects
from django.apps import AppConfig
from django.contrib import admin



class BlogConfig(AppConfig):
    name = 'blog'
'''
@admin.register(BlogDetailPage)
class BlogDetailPage(admin.ModelAdmin):
    list_display = ('id', 'custom_title', 'author', 'create_date', 'update_date', 'intro', 'tags', 'image')
'''

