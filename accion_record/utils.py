from .models import AccionRecord

class CreateAccionRecord:
  def create_instances(instances):
    objects = [
        AccionRecord(
          person_name=instance['person_name'],
          dni=instance['dni'],
          type=instance['type'],
          amount=instance['amount'],
          amount_type=instance['amount_type'],
          organization_id=instance['organization_id'],
          work_id=instance['work_id'],
          stored_object_id=instance['stored_object_id']
        ) for instance in instances
    ]
    try:
      a = AccionRecord.objects.bulk_create(objects)
      print(11111111111111111111111)
      print(a)
      print(11111111111111111111111)
      return True
    except:
      return False
    
