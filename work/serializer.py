class WorkSerializer():
    def __init__(self, objects):
      self.objects = objects

    def serialize_unit(self):
      return {
               'name': self.objects.name,
               'description': self.objects.description,
               'active': self.objects.active,
             }

    def serialize_collection(self):
      return {
              'data': [
                 {
                   'name': instance.name,
                   'description': instance.description,
                   'active': instance.active,
                 } for instance in self.objects
               ]
             }
