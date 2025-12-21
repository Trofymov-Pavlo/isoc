"""
Saved Media URL Configuration.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SavedMediaViewSet, UserCategoryViewSet

router = DefaultRouter()
router.register(r'', SavedMediaViewSet, basename='saved-media')
router.register(r'categories', UserCategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
