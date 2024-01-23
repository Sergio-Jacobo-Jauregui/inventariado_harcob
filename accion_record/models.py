from django.db import models
from organization.models import Organization
from stored_objects.models import StoredObjects
from person.models import Person
from work.models import Work
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class AccionRecord(models.Model):
  ACCION_TYPE = {
    'delivery': 'Delivery',
    'return': 'Return'
  }

  type = models.CharField(max_length=50, blank=False, null=True, choices=ACCION_TYPE)
  amount = models.IntegerField(blank=False, null=True)
  amount_type = models.CharField(max_length=50, blank=False, null=True)

  # Timestamps
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # FKs
  organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=False, null=True)
  work = models.ForeignKey(Work, on_delete=models.CASCADE, blank=False, null=True)
  stored_object = models.ForeignKey(StoredObjects, on_delete=models.CASCADE, blank=False, null=True)
  person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=False, null=True)

@receiver(pre_save, sender=AccionRecord)
def verify_type(sender, instance, **kwargs):
  keys = list(sender.ACCION_TYPE.keys())

  if not instance.type in keys:
     raise ValidationError("El campo Type debe tener un valor valido")