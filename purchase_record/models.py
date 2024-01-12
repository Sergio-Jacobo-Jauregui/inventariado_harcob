from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from organization.models import Organization

class PurchaseRecord(models.Model):
  amount = models.IntegerField(blank=True, null=True)
  amountType = models.CharField(max_length=50, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # Polymorphic
  object_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveIntegerField()
  content_object = GenericForeignKey('object_type', 'object_id')

  # Fks
  organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)

  def __str__(self):
    return self.name