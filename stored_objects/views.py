from django.http import JsonResponse
from django.http import HttpResponse
from .models import StoredObjects
from django.core.serializers import serialize
from django.contrib.auth.decorators import permission_required
from .serializer import StoredObjectsSerializer
from .utils import CreateStoredObjects
import json

# Create
@permission_required('stored_objects.add_storedobjects', raise_exception=False)
def create_stored_object(request):
  data = json.loads(request.body)
  objects = CreateStoredObjects.create_instances(data)
  if objects:
    return HttpResponse(status=200)
  else:
    return HttpResponse("Se ha enviado algun mal dato", status=400)
  
# Read
@permission_required('stored_objects.view_storedobjects', raise_exception=False)
def get_for_org(request):
  data = json.loads(request.body)
  stored_objects = StoredObjects.objects.filter(work_id=data['work_id'])
  objects_serialized = StoredObjectsSerializer.serialize(stored_objects)
  return JsonResponse(objects_serialized, safe=False)
