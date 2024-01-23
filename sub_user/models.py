from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from .managers import CustomUserManager
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .utils import AddPermissions
from organization.models import Organization

class SubUser(AbstractUser):
    STORED_OBJECTS_TYPE = {
        'only_read': 'Only_read',
        'read_write': 'Read_write',
        'read_write_delete': 'Read_write_delete'
    }

    type = models.CharField(max_length=50, choices=STORED_OBJECTS_TYPE, null=False, blank=True)

    # FKs
    if settings.DEBUG:
        parent_user_id = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)
    else:
        parent_user_id = models.ForeignKey('self', on_delete=models.RESTRICT, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=False, null=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "username"

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
@receiver(pre_save, sender=SubUser)
def verify_type(sender, instance, **kwargs):
    if instance._state.adding:
        keys = list(sender.STORED_OBJECTS_TYPE.keys())

        if not instance.type in keys:
            raise ValidationError("El campo Type debe tener un valor valido")

@receiver(post_save, sender=SubUser)
def give_permissions(sender, instance, created, **kwargs):
    if created:
        permission_assigner = AddPermissions(instance=instance, model=SubUser)
        permission_assigner.asign_permisses()
