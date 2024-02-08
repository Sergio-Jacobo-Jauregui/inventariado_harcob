from django.core.exceptions import ValidationError
from django.test import TestCase
from organization.models import Organization
from .user_factory import UserFactory
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from ..models import SubUser
from django.db.models import Q

class StoredObjectsTest(TestCase):
   def setUp(self):
      self.instance = UserFactory.build()
      self.instance.organization.save()
      self.instance.save()

      self.instance_with_permissions = UserFactory.build(organization = self.instance.organization)

      self.content_type = ContentType.objects.get_for_model(SubUser)

   def test_user_exist(self):
      self.assertIsNotNone(self.instance.id)

   def test_has_relations(self):
      self.assertIsNotNone(self.instance.organization.id)
      self.assertEqual(isinstance(self.instance.organization, Organization), True)

   def test_only_correct_type(self):
      bad_instance = UserFactory.build(
         organization=self.instance.organization,
         type='bad_type'
      )

      with self.assertRaises(ValidationError):
         bad_instance.save()

   def test_verify_only_read_permissions(self):
      self.instance_with_permissions.type = 'only_read'
      self.instance_with_permissions.save()
      permissions = Permission.objects.filter(codename='view_permission', content_type=self.content_type)

      self.assertQuerysetEqual(self.instance_with_permissions.user_permissions.all(), permissions, ordered=False)

   def test_verify_read_write_permissions(self):
      self.instance_with_permissions.type = 'read_write'
      self.instance_with_permissions.save()
      permissions = Permission.objects.filter(Q(codename='view_permission') | Q(codename='add_permission') | Q(codename='change_permission'), content_type=self.content_type)

      self.assertQuerysetEqual(self.instance_with_permissions.user_permissions.all(), permissions, ordered=False)

   def test_verify_read_write_delete_permissions(self):
      self.instance_with_permissions.type = 'read_write_delete'
      self.instance_with_permissions.save()
      permissions = Permission.objects.filter(Q(codename='view_permission') | Q(codename='add_permission') | Q(codename='change_permission') | Q(codename='delete_permission'), content_type=self.content_type)

      self.assertQuerysetEqual(self.instance_with_permissions.user_permissions.all(), permissions, ordered=False)
