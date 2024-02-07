import factory
from ..models import Person
from organization.tests.organization_factory import OrganizationFactory
import random

class PersonFactory(factory.Factory):
    class Meta:
        model = Person

    first_names = factory.Faker('first_name')
    last_names = factory.Faker('last_name')
    dni = factory.LazyAttribute(lambda _: ''.join( str(random.randint(0,9)) for _ in range(8)))
    organization = factory.SubFactory(OrganizationFactory)
