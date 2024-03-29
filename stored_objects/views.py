from django.http import JsonResponse
from django.http import HttpResponse
from .models import StoredObjects
from django.core.serializers import serialize
from django.contrib.auth.decorators import permission_required
from .serializer import StoredObjectsSerializer
from .utils import StoredObjectsCreator
import json

# Create
@permission_required('sub_user.add_permission', raise_exception=False)
def create_stored_object(request):
  data = json.loads(request.body)
  try:
    instances_creator = StoredObjectsCreator(
      new_instances=data['new_instances'],
      old_instances=data['old_instances_ids'],
      organization_id=request.user.organization_id,
      work_id=data['current_work']
    )
    message = instances_creator.add_stored_objects()
    return HttpResponse(message, status=200)
  except ValueError as e:
    return HttpResponse(f"Error: {e}", status=400)

# Read
@permission_required('sub_user.view_permission', raise_exception=False)
def get_for_work(request):
  data = json.loads(request.body)
  stored_objects = StoredObjects.objects.filter(work_id=data['work_id'])
  objects_serialized = StoredObjectsSerializer.serialize_collection(stored_objects)
  return JsonResponse(objects_serialized, safe=True)
