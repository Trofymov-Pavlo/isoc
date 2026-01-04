"""
Django project URL configuration.
Main routing for the entire project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/saved-media/', include('saved_media.urls')),
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
