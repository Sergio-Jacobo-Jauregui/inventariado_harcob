class StoredObjectsSerializer:
    def serialize_unit(instance):
      return {
               'id': instance.id,
               'name': instance.name,
               'type': instance.type,
               'stored_quantity': instance.stored_quantity,
               'quantity_in_use': instance.quantity_in_use,
               'organization_id': instance.organization_id,
               'work_id': instance.work_id,
             }

    def serialize_collection(objects):
      return {
              'data': [
                 {
                   'id': instance.id,
                   'name': instance.name,
                   'type': instance.type,
                   'stored_quantity': instance.stored_quantity,
                   'quantity_in_use': instance.quantity_in_use,
                   'organization_id': instance.organization_id,
                   'work_id': instance.work_id,
                 } for instance in objects
               ]
             }
