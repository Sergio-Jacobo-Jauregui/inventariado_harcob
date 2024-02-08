from django.test import TestCase
from organization.models import Organization
from .work_factory import WorkActive
from ..models import Work

class StoredObjectsTest(TestCase):
   def setUp(self):
      self.instance = WorkActive.build()
      self.instance.organization.save()
      self.instance.save()

   def test_work_exist(self):
      self.assertIsNotNone(self.instance.id)

   def test_has_relations(self):
      self.assertIsNotNone(self.instance.organization.id)
      self.assertEqual(isinstance(self.instance.organization, Organization), True)

   def test_name_max_lenght(self):
      self.assertAlmostEqual(Work._meta.get_field('name').max_length, 50)
