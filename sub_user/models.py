from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from .managers import CustomUserManager
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError


class SubUser(AbstractUser):
    STORED_OBJECTS_TYPE = {
        'only_read': 'Only_read',
        'read_write': 'Read_write',
        'read_write_delete': 'Read_write_delete'
    }

    type = models.CharField(max_length=50, choices=STORED_OBJECTS_TYPE, null=False, blank=True)

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
    
    def give_read_permissions(self):
        pass
    
    def give_read_write_permissions(self):
        pass
    
    def give_all_permissions(self):
        pass
    
@receiver(pre_save, sender=SubUser)
def give_permissions(sender, instance, **kwargs):
    if instance.type == 'only_read':
         instance.give_read_permissions()
    elif instance.type == 'read_write':
         instance.give_read_write_permissions()
    elif instance.type == 'read_write_delete':
         instance.give_all_permissions()
    else:
        raise ValidationError("El campo Type debe tener un valor valido")