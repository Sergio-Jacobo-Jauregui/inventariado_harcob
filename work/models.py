from django.db import models

class Work(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField()
  active = models.BooleanField()

  # Timestamps
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
