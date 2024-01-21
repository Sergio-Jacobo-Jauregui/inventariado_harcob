from django.db import models
from organization.models import Organization

class Work(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField()
  active = models.BooleanField(default=True)

  # Timestamps
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # Fks
  organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=False, null=True)

  def __str__(self):
    return self.name
