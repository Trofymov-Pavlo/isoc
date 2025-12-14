from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    remember_me = models.BooleanField(default=False)
    password_reset_token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.email
