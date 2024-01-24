from django.db import models
from organization.models import Organization
from work.models import Work
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class StoredObjects(models.Model):
  STORED_OBJECTS_TYPE = {
    'tool': 'Tool',
    'material': 'Material'
  }

  name = models.CharField(max_length=50, blank=False, null=True)
  type = models.CharField(max_length=50, blank=False, null=True, choices=STORED_OBJECTS_TYPE)
  stored_quantity = models.IntegerField(blank=False, null=True)
  quantity_in_use = models.IntegerField(blank=False, null=True)

  # Timestamps
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # FKs
  organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=False, null=True)
  work = models.ForeignKey(Work, on_delete=models.CASCADE, blank=False, null=True)

  def __str__(self):
    return  self.name if self.name else super().__str__()
  
@receiver(pre_save, sender=StoredObjects)
def verify_type(sender, instance, **kwargs):
  keys = list(sender.STORED_OBJECTS_TYPE.keys())

  if not instance.type in keys:
     raise ValidationError("El campo Type debe tener un valor valido")