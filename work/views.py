from django.http import JsonResponse
from .models import Work
from django.core.serializers import serialize
from django.contrib.auth.decorators import permission_required
import json

# Create
@permission_required('sub_user.add_permission', raise_exception=False)
def create_work(request):
  data = json.loads(request.body)
  work = Work.objects.create(
    name=data['name'],
    description=data['description'],
    active=data['active'],
    organization_id=request.user.organization_id
  )

  serialized_work = serialize('json', [work])
  return JsonResponse(serialized_work, safe=False)

# Read
@permission_required('sub_user.view_permission', raise_exception=False)
def get_for_org(request):
  works = Work.objects.filter(organization_id=request.user.organization_id)
  serialized_works = serialize('json', works)
  return JsonResponse(serialized_works, safe=False)
