"""
Saved Media API Views.

Endpoints for managing user-saved media (liked, watch later, custom categories).
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import SavedMedia, UserCategory
from .serializers import SavedMediaSerializer, UserCategorySerializer


class SavedMediaViewSet(viewsets.ModelViewSet):
    """
    API endpoint for user-saved media.
    
    Endpoints:
        GET /api/accounts/saved-media/ - List saved media for current user
        POST /api/accounts/saved-media/ - Save new media
        DELETE /api/accounts/saved-media/{id}/ - Remove saved media
        GET /api/accounts/saved-media/by-category/ - List by category
        POST /api/accounts/saved-media/toggle/ - Toggle save status
    """
    serializer_class = SavedMediaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Only return saved media for current user."""
        return SavedMedia.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Create saved media for current user."""
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get saved media filtered by category."""
        category = request.query_params.get('category', 'liked')
        media = SavedMedia.objects.filter(user=request.user, category=category).order_by('-saved_at')
        serializer = self.get_serializer(media, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def toggle(self, request):
        """
        Toggle save status for a media item.
        
        Request body:
            {
                "link": "https://...",
                "title": "Article Title",
                "source": "Source Name",
                "media_type": "article",
                "category": "liked",
                "thumbnail": "https://..."
            }
        
        Returns:
            - If item exists and was deleted: {"saved": false}
            - If item was created: {"saved": true, "id": ...}
        """
        link = request.data.get('link')
        if not link:
            return Response({'error': 'link is required'}, status=status.HTTP_400_BAD_REQUEST)

        category = request.data.get('category', 'liked')

        try:
            media = SavedMedia.objects.get(user=request.user, link=link, category=category)
            media.delete()
            return Response({'saved': False}, status=status.HTTP_200_OK)
        except SavedMedia.DoesNotExist:
            # Create new saved media
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                self.perform_create(serializer)
                return Response(
                    {'saved': True, 'id': serializer.data['id']},
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def top(self, request):
        """Get top N recently saved media (for dashboard preview)."""
        limit = request.query_params.get('limit', 3)
        category = request.query_params.get('category', 'liked')
        try:
            limit = int(limit)
        except ValueError:
            limit = 3

        media = SavedMedia.objects.filter(
            user=request.user,
            category=category
        ).order_by('-saved_at')[:limit]
        serializer = self.get_serializer(media, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def is_saved(self, request):
        """Check if a media item is saved."""
        link = request.query_params.get('link')
        category = request.query_params.get('category', 'liked')
        
        if not link:
            return Response({'error': 'link is required'}, status=status.HTTP_400_BAD_REQUEST)

        exists = SavedMedia.objects.filter(
            user=request.user,
            link=link,
            category=category
        ).exists()
        return Response({'saved': exists})


class UserCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for user-defined categories.
    
    Endpoints:
        GET /api/accounts/categories/ - List user's custom categories
        POST /api/accounts/categories/ - Create new category
        DELETE /api/accounts/categories/{id}/ - Delete category
    """
    serializer_class = UserCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Only return categories for current user."""
        return UserCategory.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Create category for current user."""
        serializer.save(user=self.request.user)
