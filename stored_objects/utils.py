from .models import StoredObjects

class CreateStoredObjects:
  def create_instances(instances):
    objects = [
        StoredObjects(
          name=instance['name'],
          type=instance['type'],
          amount=instance['amount'],
          organization_id=instance['organization_id'],
          work_id=instance['work_id']
        ) for instance in instances
    ]
    try:
      StoredObjects.objects.bulk_create(objects)
      return 'ok'
    except:
      return ''
    
