from django.db import models
from organization.models import Organization

class Person(models.Model):
  first_names = models.CharField(max_length=50)
  last_names = models.CharField(max_length=50)
  dni = models.CharField(max_length=8)

  # Fks
  organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=False, null=True)

  def __str__(self):
    return self.first_names + self.last_names
