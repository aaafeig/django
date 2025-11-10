from django.contrib import admin
from .models import Post

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'created_at', 'preview', 'views_count')
    list_filter = ('is_published',)
    search_fields = ('title', 'content',)
