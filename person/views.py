from django.http import JsonResponse
from .models import Person
from django.core.serializers import serialize
from django.contrib.auth.decorators import permission_required
import json

# Read
@permission_required('person.view_person', raise_exception=False)
def get_for_org(request):
  org_id = request.user.organization_id
  persons = Person.objects.filter(organization_id=org_id)
  serialized_persons = serialize('json', persons)
  return JsonResponse(serialized_persons, safe=False)
