"""
User Model.

Custom user model extending Django's AbstractUser.
Uses email as the primary authentication field.
"""
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Custom user model with email-based authentication.
    
    Fields:
        email: Unique email address used for login
        remember_me: Flag for persistent sessions
        password_reset_token: Token for password reset flow
    """
    email = models.EmailField(unique=True)
    remember_me = models.BooleanField(default=False)
    password_reset_token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email
