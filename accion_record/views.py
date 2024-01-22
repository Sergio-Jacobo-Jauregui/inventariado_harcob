from django.http import HttpResponse
from django.shortcuts import render
import json
from .utils import CreateAccionRecord

def create_accion_record(request):
  data = json.loads(request.body)
  status = CreateAccionRecord.create_instances(data)
  if status:
    return HttpResponse(status=200)
  else:
    return HttpResponse("Se ha enviado algun mal dato", status=400)