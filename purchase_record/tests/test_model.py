from django.db import IntegrityError
from django.test import TestCase
from organization.models import Organization
from work.models import Work
from stored_objects.models import StoredObjects
from .purchase_record_factory import PurchaseRecordFactory

class PurchaseRecordTest(TestCase):
   def setUp(self):
      self.instance = PurchaseRecordFactory.build()
      self.instance.organization.save()
      self.instance.work.save()
      self.instance.stored_object.save()
      self.instance.save()

   def test_purchase_record_exist(self):
      self.assertIsNotNone(self.instance.id)

   def test_has_relations(self):
      self.assertIsNotNone(self.instance.organization.id)
      self.assertEqual(isinstance(self.instance.organization, Organization), True)

      self.assertIsNotNone(self.instance.work.id)
      self.assertEqual(isinstance(self.instance.work, Work), True)

      self.assertIsNotNone(self.instance.stored_object.id)
      self.assertEqual(isinstance(self.instance.stored_object, StoredObjects), True)

   def test_added_quantity_only_positive(self):
      negative_instance = PurchaseRecordFactory.build(
         added_quantity=-1,
         work=self.instance.work,
         organization=self.instance.work.organization,
         stored_object=self.instance.stored_object
      )

      with self.assertRaises(IntegrityError):
         negative_instance.save()
