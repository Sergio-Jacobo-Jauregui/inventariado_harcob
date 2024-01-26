class PersonSerializer:
    def serialize_unit(instance):
      return {
               'id': instance.id,
               'first_names': instance.first_names,
               'last_names': instance.last_names,
               'dni': instance.dni,
             }

    def serialize_collection(objects):
      return {
              'data': [
                 {
                   'id': instance.id,
                   'first_names': instance.first_names,
                   'last_names': instance.last_names,
                   'dni': instance.dni,
                 } for instance in objects
               ]
             }
