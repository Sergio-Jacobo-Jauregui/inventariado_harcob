from .models import AccionRecord
from django.db import transaction
from stored_objects.utils import StoredObjectsUpdater

@transaction.atomic
class AccionRecordCreator:
  def __init__(self, current_work, objects, organization_id):
    self.current_work = current_work
    self.objects = objects
    self.organization_id = organization_id

  def create_instances(self):
    self.create_accion_records()
    self.increase_or_decrease_objects()

  def create_accion_records(self):
    objects = [
        AccionRecord(
          type=instance['type'],
          quantity=instance['quantity'],
          quantity_type=instance['quantity_type'],

          organization_id=instance['organization_id'],
          work_id=instance['work_id'],
          stored_object_id=instance['stored_object_id'],
          person_id=instance['person_id']
        ) for instance in self.objects
    ]
    try:
      AccionRecord.objects.bulk_create(objects)
      return 'Instancias creadas correctamente'
    except:
      raise ValueError("Hubo un error al crear las acciones")
    
  def increase_or_decrease_objects(self):
    pass
    # stored_objects = [
    #   for i in self.objects
    # ]


    # object_stored_updater = StoredObjectsUpdater(
    #   objects=stored_objects
    # )
    # object_stored_updater.update_instances()