from .models import StoredObjects
from purchase_record.utils import PurchaseRecordCreator
from django.db import transaction

class StoredObjectsCreator:
  def __init__(self, new_instances, old_instances, organization_id, work_id):
    self.new_instances = new_instances
    self.old_instances = old_instances
    self.organization_id = organization_id
    self.work_id = work_id

  @transaction.atomic
  def add_stored_objects(self):
    new_objects = self.create_new_objects()
    self.update_objects()
    status = self.create_purchase_records(new_objects + self.old_instances)
    return status

  def check_instance_consistency_create(self):
    stored_quantities = [
        instance['stored_quantity'] for instance in self.new_instances
      ]

    if not all( quantity>=0 for quantity in stored_quantities ):
      raise ValueError("Alguna cantidad en los nuevos es negativa")
    
    instance_types = [
        instance['type'] for instance in self.new_instances
      ]

    if not all( instance_type=='tool' or instance_type=='material' for instance_type in instance_types ):
      raise ValueError("Alguna instancia nueva no tiene un tipo correcto")
    
  def create_new_objects(self):
    self.check_instance_consistency_create()
    objects = [
      StoredObjects(
        name=instance['name'],
        type=instance['type'],
        stored_quantity=instance['stored_quantity'],
        quantity_in_use=0,
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
        'added_quantity': new_object.stored_quantity
      } for new_object in created_objects
    ]

  def check_instance_consistency_update(self):
    id_list = [object['id'] for object in self.old_instances]
    stored_objects = StoredObjects.objects.filter(id__in=id_list)

    if len(stored_objects) != len(id_list):
      raise ValueError("Se paso un id que no existe para actualizar")

    if len(id_list) != len(set(id_list)):
      raise ValueError("Se paso un objecto id duplicado")

    return stored_objects

  def update_objects(self):
    stored_objects = self.check_instance_consistency_update()

    update_stored_objects = []
    for stored_object in list(stored_objects):
      for original_object in self.old_instances:
        if stored_object.id == original_object['id']:
          update_stored_objects.append(
            StoredObjects(
            id=stored_object.id,
            stored_quantity=stored_object.stored_quantity + original_object['added_quantity']
            )
          )
          break

    try:
      StoredObjects.objects.bulk_update(update_stored_objects, ['stored_quantity'])
    except:
      raise ValueError("Hay un mal dato en los viejos objectos")

  def create_purchase_records(self, data):
    return PurchaseRecordCreator.create_instances(
      data=data,
      organization_id=self.organization_id,
      work_id=self.work_id
    )

# todo: add validation not negative number and granularize
class StoredObjectsUpdater:
  def update_instances(objects):
    ids = [ instance['stored_object_id'] for instance in objects ]
    stored_objects = StoredObjects.objects.filter(id__in=ids)

    update_stored_objects = []
    for stored_object in list(stored_objects):
      for object in objects:
        if stored_object.id == object['stored_object_id']:
          if object['type'] ==  'delivery':
            update_instance = StoredObjects(
              id=stored_object.id,
              stored_quantity=stored_object.stored_quantity - object['quantity'],
              quantity_in_use=stored_object.quantity_in_use + object['quantity']
            )
          else:
            update_instance = StoredObjects(
              id=stored_object.id,
              stored_quantity=stored_object.stored_quantity + object['quantity'],
              quantity_in_use=stored_object.quantity_in_use - object['quantity']
            )

          update_stored_objects.append(update_instance)  
          break
    try:
      StoredObjects.objects.bulk_update(update_stored_objects, ['stored_quantity', 'quantity_in_use'])
    except:
      raise ValueError("Hay algun problema actualizando los stored objects")
    
    return 'Instancias creadas correctamente'
    
    