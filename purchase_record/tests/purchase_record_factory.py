import factory
from ..models import PurchaseRecord
from organization.tests.organization_factory import OrganizationFactory
from work.tests.work_factory import WorkActive
from stored_objects.tests.stored_objects_factory import StoredObjectsFactory
import random

class PurchaseRecordFactory(factory.Factory):
    class Meta:
        model = PurchaseRecord

    # Attributes
    added_quantity = random.randint(0, 100)

    # Fks
    organization = factory.SubFactory(OrganizationFactory)
    work = factory.SubFactory(WorkActive, organization=factory.SelfAttribute('..organization'))
    stored_object = factory.SubFactory(
        StoredObjectsFactory,
        organization=factory.SelfAttribute('..organization'),
        work=factory.SelfAttribute('..work')
    )
