"""
ASGI config for isoc_auth project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'isoc_auth.settings')

application = get_asgi_application()
