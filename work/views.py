
from django.http import JsonResponse
from .models import Work
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
import json

# Create
@permission_required('work.add_work', raise_exception=False)
@login_required
def create_work(request):
  data = json.loads(request.body)
  works = Work.objects.create(
    name=data.name,
    description=data.description,
    active=data.active,
    organization_id=request.user.organization_id
  )

  serialized_work = serialize('json', works)
  return JsonResponse(serialized_work, safe=False)

# Read
@permission_required('work.view_work', raise_exception=False)
@login_required
def get_for_org(request):
  works = Work.objects.filter(organization_id=request.user.organization_id)
  serialized_works = serialize('json', works)
  return JsonResponse(serialized_works, safe=False)
