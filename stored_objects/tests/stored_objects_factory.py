import factory
from ..models import StoredObjects
from organization.tests.organization_factory import OrganizationFactory
from work.tests.work_factory import WorkActive
import factory.fuzzy

STORED_OBJECTS_TYPE = ['tool', 'material']

class StoredObjectsFactory(factory.Factory):
    class Meta:
        model = StoredObjects

    # Attributes
    name = factory.Faker('name')
    type = factory.Faker('random_element', elements=STORED_OBJECTS_TYPE)
    stored_quantity = factory.fuzzy.FuzzyInteger(0, 100)
    quantity_in_use = factory.fuzzy.FuzzyInteger(0, 100)

    # Fks
    organization = factory.SubFactory(OrganizationFactory)
    work = factory.SubFactory(WorkActive, organization=factory.SelfAttribute('..organization'))
