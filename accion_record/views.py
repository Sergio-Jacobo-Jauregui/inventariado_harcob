from django.http import HttpResponse
import json
from .utils import AccionRecordCreator
from django.contrib.auth.decorators import permission_required

# Create
@permission_required('sub_user.add_permission', raise_exception=False)
def create_accion_record(request):
  try:
    data = json.loads(request.body)
    creator = AccionRecordCreator(
      current_work=data['current_work'],
      objects=data['objects'],
      organization_id=data['objects']
    )
    message = creator.create_instances(data=data)
    return HttpResponse(message, status=200)
  except:
    return HttpResponse("Se ha enviado algun mal dato", status=400)