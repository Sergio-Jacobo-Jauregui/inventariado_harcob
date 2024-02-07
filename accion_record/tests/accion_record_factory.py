import factory
from ..models import AccionRecord
from organization.tests.organization_factory import OrganizationFactory
from work.tests.work_factory import WorkActive
from stored_objects.tests.stored_objects_factory import StoredObjectsFactory
from person.tests.person_factory import PersonFactory

class AccionRecordFactory(factory.Factory):
    class Meta:
        model = AccionRecord

    # Attributes
    type = factory.Faker('first_name')
    quantity = factory.Faker('last_name')
    quantity_type = factory.Faker('text', max_nb_chars=50)

    # Fks
    organization = factory.SubFactory(OrganizationFactory)
    work = factory.SubFactory(WorkActive)
    stored_object = factory.SubFactory(StoredObjectsFactory)
    person = factory.SubFactory(PersonFactory)
