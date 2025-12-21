"""
Saved Media Models.

Models for user-saved media items (liked, watch later, custom categories).
"""
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class SavedMediaType(models.TextChoices):
    """Media type choices."""
    ARTICLE = 'article', 'Article'
    VIDEO = 'video', 'Vidéo'
    LIVE = 'live', 'En Direct'


class SavedMediaCategory(models.TextChoices):
    """Default category choices (users can create custom ones)."""
    LIKED = 'liked', 'Likés'
    WATCH_LATER = 'watch_later', 'À regarder plus tard'


class SavedMedia(models.Model):
    """
    User-saved media items (liked, watch later, custom collections).
    
    Fields:
        user: FK to User
        link: URL of the media (unique per user)
        title: Media title
        source: Media source/channel
        media_type: article/video/live
        category: Default category (liked/watch_later) or custom
        thumbnail: Thumbnail URL
        saved_at: Timestamp when saved
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_media')
    link = models.URLField()
    title = models.CharField(max_length=500)
    source = models.CharField(max_length=255, blank=True, null=True)
    media_type = models.CharField(max_length=20, choices=SavedMediaType.choices, default=SavedMediaType.ARTICLE)
    category = models.CharField(max_length=100, default=SavedMediaCategory.LIKED)
    thumbnail = models.URLField(blank=True, null=True)
    saved_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'link', 'category')
        ordering = ['-saved_at']

    def __str__(self):
        return f"{self.user.email} - {self.title[:50]}"


class UserCategory(models.Model):
    """
    Custom user-defined categories for organizing saved media.
    
    Fields:
        user: FK to User
        name: Category name (e.g., "À lire demain", "Podcast favoris")
        color: Hex color for UI
        created_at: Timestamp
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='custom_categories')
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='#2f0538')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'name')
        ordering = ['created_at']

    def __str__(self):
        return f"{self.user.email} - {self.name}"
