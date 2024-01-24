from .models import StoredObjects
from purchase_record.utils import PurchaseRecordCreator
from django.db import transaction

@transaction.atomic
class StoredObjectsCreator:
  def __init__(self, new_instances, old_instances, organization_id, work_id):
    self.new_instances = new_instances
    self.old_instances = old_instances
    self.organization_id = organization_id
    self.work_id = work_id

  def add_stored_objects(self):
    new_objects = self.create_new_objects()
    self.update_objects()
    status = self.create_purchase_records(new_objects + self.old_instances)
    return status

  def create_new_objects(self):
    objects = [
      StoredObjects(
        name=instance['name'],
        type=instance['type'],
        amount=instance['amount'],
        organization_id=self.organization_id,
        work_id=self.work_id
      ) for instance in self.new_instances
    ]

    try:
      created_objects = StoredObjects.objects.bulk_create(objects)
    except:
      raise ValueError("Hay un mal dato en los nuevos objectos")
    
    return [
      { 
        'id': new_object.id,
        'amount': new_object.amount
      } for new_object in created_objects
    ]

  def update_objects(self):
    id_list = [object['id'] for object in self.old_instances]
    stored_objects = StoredObjects.objects.filter(id__in=id_list)

    if len(stored_objects) != len(id_list):
      raise ValueError("Se paso un id que no existe para actualizar")
  
    update_stored_objects = []
    for stored_object in list(stored_objects):
      for original_object in self.old_instances:
        if stored_object.id == original_object['id']:
          update_stored_objects.append(
            StoredObjects(
            id=stored_object.id,
            amount=stored_object.amount + original_object['amount']
            )
          )
          break

    try:
      StoredObjects.objects.bulk_update(update_stored_objects, ['amount'])
    except:
      raise ValueError("Hay un mal dato en los viejos objectos")

  def create_purchase_records(self, data):
    return PurchaseRecordCreator.create_instances(
      data,
      self.organization_id,
      self.work_id
    )

@transaction.atomic
class StoredObjectsUpdater:
  def __init__(self, objects):
    self.objects = objects

  def update_instances(self):
    pass