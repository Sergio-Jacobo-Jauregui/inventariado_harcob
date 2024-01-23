from django.db import models

class Person(models.Model):
  first_names = models.CharField(max_length=50)
  last_names = models.CharField(max_length=50)
  dni = models.CharField(max_length=8)

  def __str__(self):
    self.first_names + self.last_names
