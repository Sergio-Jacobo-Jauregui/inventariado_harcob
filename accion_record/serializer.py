class AccionRecordSerializer:
    def serialize_unit(instance):
      return {
               'id': instance.id,
               'type': instance.type,
               'quantity': instance.quantity,
               'quantity_type': instance.quantity_type,
               'created_at': instance.created_at,
               'stored_object': instance.stored_object,
               'person': instance.person,
             }

    def serialize_collection(objects):
      return {
              'data': [
                 {
                   'id': instance.id,
                   'type': instance.type,
                   'quantity': instance.quantity,
                   'quantity_type': instance.quantity_type,
                   'created_at': instance.created_at,
                   'stored_object': instance.stored_object,
                   'person': instance.person,
                 } for instance in objects
               ]
             }
