from django.db import models
from organization.models import Organization
from object.models import Tool

class UsageRecord(models.Model):
  person_name = models.IntegerField(blank=True, null=True)
  use_date = models.DateTimeField()
  return_date = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # Fks
  organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
  tool = models.ForeignKey(Tool, on_delete=models.CASCADE, blank=True, null=True)
