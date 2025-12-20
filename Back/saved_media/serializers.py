"""
Saved Media Serializers.
"""
from rest_framework import serializers
from .models import SavedMedia, UserCategory


class SavedMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedMedia
        fields = ('id', 'link', 'title', 'source', 'media_type', 'category', 'thumbnail', 'saved_at')
        read_only_fields = ('id', 'saved_at')


class UserCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCategory
        fields = ('id', 'name', 'color', 'created_at')
        read_only_fields = ('id', 'created_at')
