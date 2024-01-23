from django.http import HttpResponse
import json
from .utils import CreateAccionRecord
from django.contrib.auth.decorators import permission_required

# Create
@permission_required('sub_user.add_permission', raise_exception=False)
def create_accion_record(request):
  data = json.loads(request.body)
  status = CreateAccionRecord.create_instances(data)
  if status:
    return HttpResponse(status=200)
  else:
    return HttpResponse("Se ha enviado algun mal dato", status=400)