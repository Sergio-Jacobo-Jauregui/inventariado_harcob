from django.db import models
from organization.models import Organization
from work.models import Work

class StoredObjects(models.Model):
  name = models.CharField(max_length=50, blank=False, null=True)
  type = models.CharField(max_length=50, blank=False, null=True)
  amount = models.IntegerField()

  # Timestamps
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # FKs
  organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=False, null=True)
  work = models.ForeignKey(Work, on_delete=models.CASCADE, blank=False, null=True)

  def __str__(self):
    return  self.name