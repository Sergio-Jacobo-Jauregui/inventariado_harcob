from django.http import HttpResponse
import json
from accion_record.serializer import AccionRecordSerializer
from .utils import AccionRecordCreator
from django.contrib.auth.decorators import permission_required
from .models import AccionRecord
from django.http import JsonResponse

# Create
@permission_required('sub_user.add_permission', raise_exception=False)
def create_accion_record(request):
  try:
    data = json.loads(request.body)
    creator = AccionRecordCreator(
      current_work=data['current_work'],
      objects=data['objects'],
      organization_id=request.user.organization_id
    )
    message = creator.create_instances()
    return HttpResponse(message, status=200)
  except ValueError as e:
    return HttpResponse(f"Error: {e}", status=400)

# Read
@permission_required('sub_user.view_permission', raise_exception=False)
def get_for_work(request):
  data = json.loads(request.body)
  accion_records = AccionRecord.objects.filter(work_id=data['work_id'])
  serialized_accion_records = AccionRecordSerializer.serialize_collection(accion_records)
  return JsonResponse(serialized_accion_records, safe=True)