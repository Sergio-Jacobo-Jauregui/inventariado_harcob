import factory
from ..models import AccionRecord
from organization.tests.organization_factory import OrganizationFactory
from work.tests.work_factory import WorkActive
from stored_objects.tests.stored_objects_factory import StoredObjectsFactory
from person.tests.person_factory import PersonFactory
import random

ACCION_TYPE = ['delivery', 'return']

class AccionRecordFactory(factory.Factory):
    class Meta:
        model = AccionRecord

    # Attributes
    type = factory.Faker('random_element', elements=ACCION_TYPE)
    quantity = random.randint(0, 100)
    quantity_type = factory.Faker('text', max_nb_chars=50)

    # Fks
    organization = factory.SubFactory(OrganizationFactory)
    work = factory.SubFactory(WorkActive)
    stored_object = factory.SubFactory(StoredObjectsFactory)
    person = factory.SubFactory(PersonFactory)
