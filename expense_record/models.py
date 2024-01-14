from django.db import models
from organization.models import Organization
from object.models import Material
from purchase_record.models import PurchaseRecord
from object.models import Work

class ExpenseRecord(models.Model):
  amount = models.IntegerField(blank=True, null=True)
  amountType = models.CharField(max_length=50, blank=True, null=True)
  expense_date = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # Fks
  organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
  material = models.ForeignKey(Material, on_delete=models.CASCADE, blank=True, null=True)
  purchase_record = models.ForeignKey(PurchaseRecord, on_delete=models.CASCADE, blank=True, null=True)
  work = models.ForeignKey(Work, on_delete=models.CASCADE)
