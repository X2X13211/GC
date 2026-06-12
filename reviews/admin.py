from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):  
    list_display = ('title', 'id', 'is_published', 'created_at', 'updated_at', 'author')
    list_filter = ('is_published', 'created_at', 'author')
    search_fields = ('title', 'content')
    readonly_fields = ('id', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
