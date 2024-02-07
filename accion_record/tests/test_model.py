from django.test import TestCase
from organization.models import Organization
from work.models import Work
from stored_objects.models import StoredObjects
from person.models import Person
from .accion_record_factory import AccionRecordFactory
from work.tests.work_factory import WorkFactory
from person.tests.person_factory import PersonFactory
from stored_objects.tests.stored_objects_factory import StoredObjectsFactory
import logging

logging.basicConfig(level=logging.WARNING)

class AccionRecordTest(TestCase):
   def setUp(self):
      self.work = WorkFactory.create()
      self.work.organization.save()
      self.work.save()

      self.person = PersonFactory.create(
         organization=self.work.organization
      )
      self.person.save()

      self.stored_object = StoredObjectsFactory.create(
         work=self.work,
         organization=self.work.organization
      )
      self.stored_object.save()

      self.instance = AccionRecordFactory.create(
         work=self.work,
         organization=self.work.organization,
         stored_object=self.stored_object,
         person=self.person
      )
      self.instance.save()

   def test_accion_record_exist(self):
      self.assertIsNotNone(self.instance.id)

   def test_has_relations(self):
      self.assertIsNotNone(self.instance.organization.id)
      self.assertEqual(isinstance(self.instance.organization, Organization), True)

      self.assertIsNotNone(self.instance.work.id)
      self.assertEqual(isinstance(self.instance.work, Work), True)

      self.assertIsNotNone(self.instance.stored_object.id)
      self.assertEqual(isinstance(self.instance.stored_object, StoredObjects), True)

      self.assertIsNotNone(self.instance.person.id)
      self.assertEqual(isinstance(self.instance.person, Person), True)

   def test_max_lenght_in_columns(self):
      self.assertEqual(self.instance._meta.get_field('type').max_length, 8)
      self.assertEqual(self.instance._meta.get_field('quantity_type').max_length, 20)

   def test_quantity_only_positive(self):
      negative_instance = AccionRecordFactory.build(
         quantity=-1,
         work=self.work,
         organization=self.work.organization
      )

      with self.assertRaises(ValueError):
         negative_instance.save()
