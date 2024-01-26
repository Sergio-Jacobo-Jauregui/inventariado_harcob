from django.db import models
from organization.models import Organization
from stored_objects.models import StoredObjects
from work.models import Work

class PurchaseRecord(models.Model):
  added_quantity = models.PositiveIntegerField(blank=False, null=True)

  # Timestamps
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # Fks
  organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=False, null=True)
  work = models.ForeignKey(Work, on_delete=models.CASCADE, blank=False, null=True)
  stored_object = models.ForeignKey(StoredObjects, on_delete=models.CASCADE, blank=False, null=True)

  def __str__(self):
    return 'Creado el: ' + str(self.created_at)