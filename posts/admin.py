from django.contrib import admin
from .models import Post, Comment, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'created_at', 'likes_count')
    list_filter = ('is_published', 'created_at', 'author')
    search_fields = ('title', 'content')
    readonly_fields = ('id', 'created_at', 'updated_at', 'slug')
    prepopulated_fields = {}

    def likes_count(self, obj):
        return obj.likes.count()
    likes_count.short_description = 'Лайки'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at', 'short_body')
    list_filter = ('created_at', 'author')
    search_fields = ('body', 'author__username')
    readonly_fields = ('created_at',)

    def short_body(self, obj):
        return obj.body[:60] + '...' if len(obj.body) > 60 else obj.body
    short_body.short_description = 'Текст'


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    list_filter = ('created_at',)
