"""
Saved Media Admin Configuration.
"""
from django.contrib import admin
from .models import SavedMedia, UserCategory


@admin.register(SavedMedia)
class SavedMediaAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'category', 'media_type', 'saved_at')
    list_filter = ('category', 'media_type', 'saved_at')
    search_fields = ('user__email', 'title', 'link')
    readonly_fields = ('saved_at', 'updated_at')


@admin.register(UserCategory)
class UserCategoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'color', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__email', 'name')
    readonly_fields = ('created_at',)
