from django.contrib import admin
from .models import Post, Category, Comment

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'category', 'publish', 'update',
    )
    prepopulated_fields = {'slug': ('title', )}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post', 'author', 'publish', 'update'
    )