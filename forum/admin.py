from django.contrib import admin
from .models import Post, Category

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'publish', 'update'
    )
    prepopulated_fields = {'slug': ('title', )}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )