from django.test import TestCase
from ..models import Organization
from .organization_factory import OrganizationFactory

class OrganizationTest(TestCase):
   def setUp(self):
      self.instance = OrganizationFactory.create()
      self.instance.save()

   def test_organization_exist(self):
      self.assertIsNotNone(self.instance.id)

   def test_max_lenght_in_columns(self):
      self.assertEqual(self.instance._meta.get_field('name').max_length, 50)
