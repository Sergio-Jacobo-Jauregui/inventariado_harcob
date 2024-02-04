import factory
from ..models import Organization

class OrganizationFactory(factory.Factory):
    class Meta:
        model = Organization

    name = factory.Faker('name')
