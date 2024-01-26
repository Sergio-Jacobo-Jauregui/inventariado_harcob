from django.http import JsonResponse
from .models import Person
from django.core.serializers import serialize
from django.contrib.auth.decorators import permission_required
import json
from .serializer import PersonSerializer

# Create
@permission_required('sub_user.add_permission', raise_exception=False)
def create_person(request):
  data = json.loads(request.body)
  new_person = Person.objects.create(
    first_names=data['first_names'],
    last_names=data['last_names'],
    dni= str(data['dni']),
    organization_id= request.user.organization_id
  )
  serialized_person = PersonSerializer.serialize_unit(new_person)
  return JsonResponse(serialized_person, safe=True)

# Read
@permission_required('sub_user.view_permission', raise_exception=False)
def get_for_org(request):
  org_id = request.user.organization_id
  persons = Person.objects.filter(organization_id=org_id)
  serialized_persons = PersonSerializer.serialize_collection(persons)
  return JsonResponse(serialized_persons, safe=True)
