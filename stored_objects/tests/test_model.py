from django.db import IntegrityError
from django.test import TestCase
from organization.models import Organization
from work.models import Work
from .stored_objects_factory import StoredObjectsFactory

class StoredObjectsTest(TestCase):
   def setUp(self):
      self.instance = StoredObjectsFactory.build()
      self.instance.organization.save()
      self.instance.work.save()
      self.instance.save()

   def test_stored_objects_exist(self):
      self.assertIsNotNone(self.instance.id)

   def test_has_relations(self):
      self.assertIsNotNone(self.instance.organization.id)
      self.assertEqual(isinstance(self.instance.organization, Organization), True)

      self.assertIsNotNone(self.instance.organization.id)
      self.assertEqual(isinstance(self.instance.work, Work), True)

   def test_quantity_in_use_only_positive(self):
      negative_instance = StoredObjectsFactory.build(
         work=self.instance.work,
         organization=self.instance.organization,
         quantity_in_use=-1,
         stored_quantity=1
      )

      with self.assertRaises(IntegrityError):
         negative_instance.save()

   def test_stored_quantity_only_positive(self):
      negative_instance = StoredObjectsFactory.build(
         work=self.instance.work,
         organization=self.instance.organization,
         quantity_in_use=1,
         stored_quantity=-1
      )

      with self.assertRaises(IntegrityError):
         negative_instance.save()
