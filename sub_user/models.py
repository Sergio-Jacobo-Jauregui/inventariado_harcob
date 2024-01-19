from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from .managers import CustomUserManager

class SubUser(AbstractUser):
    if settings.DEBUG:
        parent_user_id = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)
    else:
        parent_user_id = models.ForeignKey('self', on_delete=models.RESTRICT, null=True, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "username"

    objects = CustomUserManager()

    def __str__(self):
        return self.username
