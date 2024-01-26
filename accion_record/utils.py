from .models import AccionRecord
from django.db import transaction
from stored_objects.utils import StoredObjectsUpdater
from django.core.exceptions import ValidationError

class AccionRecordCreator:
  def __init__(self, current_work, objects, organization_id):
    self.current_work = current_work
    self.objects = objects
    self.organization_id = organization_id

  @transaction.atomic
  def create_instances(self):
    self.create_accion_records()
    message = self.update_object_stored()
    return message

  def verify_accion_record_integrity(self):
    quantities = [ instance['quantity'] for instance in self.objects]
    if not all(quantity>=0 for quantity in quantities):
      raise ValidationError("Algun campo quantity es negativo")
    
    types = [ instance['type'] for instance in self.objects]
    if not all( type=='delivery' or type=='return' for type in types ):
      raise ValidationError("Algun campo type no es valido")

  def create_accion_records(self):
    self.verify_accion_record_integrity()

    objects = [
        AccionRecord(
          type=instance['type'],
          quantity=instance['quantity'],
          quantity_type=instance['quantity_type'],

          organization_id=self.organization_id,
          work_id=instance['work_id'],
          stored_object_id=instance['stored_object_id'],
          person_id=instance['person_id']
        ) for instance in self.objects
    ]

    try:
      AccionRecord.objects.bulk_create(objects)
    except:
      raise ValueError("Hubo un error al crear las acciones")
    
  def update_object_stored(self):
    objects = [ 
      {
        "type":instance['type'],
        "quantity":instance['quantity'],
        "stored_object_id":instance['stored_object_id'],
      } for instance in self.objects
    ]
    message = StoredObjectsUpdater.update_instances(objects)
    return message