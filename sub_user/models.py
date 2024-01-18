from django.contrib.auth.models import AbstractUser
from django.db import models

class SubUser(AbstractUser):
    parent_user_id = models.ForeignKey('self', on_delete=models.RESTRICT, null=True, blank=True)

    def __str__(self):
        return self.username
