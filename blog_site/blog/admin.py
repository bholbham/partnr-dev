from django.contrib import admin
from .models import BlogPost,Comment
# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title','author','timestamp']
    search_fields=['title','author_username']
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author','blog_post']
    search_fields=['author_username','blog_post_title']