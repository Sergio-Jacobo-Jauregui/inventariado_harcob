from django.shortcuts import render
from django.http import JsonResponse
from .models import Organization
from django.core.serializers import serialize

def get_all(request):
  orgs = Organization.objects.all()
  orgs_serializado = serialize('json', orgs)
  return JsonResponse(orgs_serializado, safe=False)