from django.db import models
from organization.models import Organization

class Tool(models.Model):
  name = models.CharField(max_length=50, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)

  def __str__(self):
    return self.name
  

class Material(models.Model):
  name = models.CharField(max_length=50, blank=True, null=True)
  size = models.CharField(max_length=20, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)

  def __str__(self):
    return self.name