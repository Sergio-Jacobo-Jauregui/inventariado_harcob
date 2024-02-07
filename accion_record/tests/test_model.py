from django.test import TestCase
from organization.models import Organization
from .accion_record_factory import AccionRecordFactory

class AccionRecordTest(TestCase):
   def setUp(self):
      self.instance = AccionRecordFactory.build()
      self.instance.organization.save()
      self.instance.work.save()
      self.instance.stored_object.save()
      self.instance.person.save()
      self.instance.save()

   def test_person_exist(self):
      self.assertIsNotNone(self.instance.id)

   def test_has_organization(self):
      self.assertIsNotNone(self.instance.organization.id)
      self.assertEqual(isinstance(self.instance.organization, Organization), True)

   def test_max_lenght_in_columns(self):
      self.assertEqual(self.instance._meta.get_field('first_names').max_length, 50)
      self.assertEqual(self.instance._meta.get_field('last_names').max_length, 50)
      self.assertEqual(self.instance._meta.get_field('dni').max_length, 8)
