class WorkSerializer:
    def serialize_unit(instance):
      return {
               'id': instance.id,
               'name': instance.name,
               'description': instance.description,
               'active': instance.active,
             }

    def serialize_collection(objects):
      return {
              'data': [
                 {
                   'id': instance.id,
                   'name': instance.name,
                   'description': instance.description,
                   'active': instance.active,
                 } for instance in objects
               ]
             }
