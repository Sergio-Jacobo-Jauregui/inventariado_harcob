from django.http import JsonResponse
from .models import StoredObjects
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from .serializer import StoredObjectsSerializer
import json

# ToDo

# Create
# @permission_required('stored_objects.add_storedobjects', raise_exception=False)
# @login_required
# def create_stored_object(request):
#   data = json.loads(request.body)
#   works = Work.objects.create(
#     name=data.name,
#     description=data.description,
#     active=data.active,
#     organization_id=request.user.organization_id
#   )

#   serialized_work = serialize('json', works)
#   return JsonResponse(serialized_work, safe=False)

# Read
@permission_required('stored_objects.view_storedobjects', raise_exception=False)
@login_required
def get_for_org(request):
  data = json.loads(request.body)
  stored_objects = StoredObjects.objects.filter(work_id=data.work_id)
  objects_serialized = StoredObjectsSerializer.serialize(stored_objects)
  return JsonResponse(objects_serialized, safe=False)
