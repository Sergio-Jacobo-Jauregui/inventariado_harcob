from django.test import TestCase
from .models import Person
from organization.models import Organization

class PersonTest(TestCase):
  def test_creacion_modelo(self):
    organization = Organization.objects.create(
       name="org"
    )
    
    person = Person.objects.create(
       first_names="Name Name2",
       last_names="LastName LastName2",
       dni='11111111',
       organization_id=organization.id
    )

    self.assertIsNotNone(person.id)