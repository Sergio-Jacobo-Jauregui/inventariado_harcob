import factory
from ..models import Person
from organization.tests.organization_factory import OrganizationFactory

class PersonFactory(factory.Factory):
    class Meta:
        model = Person

    first_names = factory.Faker('first_name')
    last_names = factory.Faker('last_name')
    dni = False
    organization = factory.SubFactory(OrganizationFactory)
