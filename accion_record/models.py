from django.db import models
from organization.models import Organization
from stored_objects.models import StoredObjects
from work.models import Work

class AccionRecord(models.Model):
  person_name = models.CharField(max_length=50, blank=False, null=True)
  type = models.CharField(max_length=50, blank=False, null=True)
  amount = models.IntegerField(blank=False, null=True)
  amount_type = models.CharField(max_length=50, blank=False, null=True)

  # Timestamps
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # FKs
  organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=False, null=True)
  work = models.ForeignKey(Work, on_delete=models.CASCADE, blank=False, null=True)
  stored_object = models.ForeignKey(StoredObjects, on_delete=models.CASCADE, blank=False, null=True)