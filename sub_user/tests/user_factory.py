import factory
from ..models import SubUser
from organization.tests.organization_factory import OrganizationFactory
from work.tests.work_factory import WorkActive
import factory.fuzzy

STORED_OBJECTS_TYPE = ['only_read', 'read_write', 'read_write_delete']

class UserFactory(factory.Factory):
    class Meta:
        model = SubUser

    # Attributes
    username = factory.Faker('name')
    type = factory.Faker('random_element', elements=STORED_OBJECTS_TYPE)
    email = factory.Faker('email')
    password = factory.Faker('name')

    # Fks
    organization = factory.SubFactory(OrganizationFactory)
