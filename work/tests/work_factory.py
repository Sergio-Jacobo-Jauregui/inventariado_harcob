import factory
from ..models import Work
from organization.tests.organization_factory import OrganizationFactory

class WorkFactory(factory.Factory):
    class Meta:
        model = Work

    # Attributes
    name = factory.Faker('name')
    description = factory.Faker('text', max_nb_chars=40)

    # Fks
    organization = factory.SubFactory(OrganizationFactory)

class WorkActive(WorkFactory):
    active = True

class WorkInactive(WorkFactory):
    active = False