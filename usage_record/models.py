from django.db import models
from organization.models import Organization
from object.models import Tool
from object.models import Work

class UsageRecord(models.Model):
  person_name = models.IntegerField(blank=True, null=True)
  use_date = models.DateTimeField()
  return_date = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # Fks
  organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
  tool = models.ForeignKey(Tool, on_delete=models.CASCADE, blank=True, null=True)
  work = models.ForeignKey(Work, on_delete=models.CASCADE)

  def __str__(self):
    return 'Usado por: ' + self.person_name