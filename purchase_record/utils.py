from .models import PurchaseRecord

class PurchaseRecordCreator:
  def create_instances(data, organization_id, work_id):
    objects = [
        PurchaseRecord(
          stored_object_id=instance['id'],
          quantity=instance['quantity'],
          organization_id=organization_id,
          work_id=work_id
        ) for instance in data
    ]
    try:
      objects = PurchaseRecord.objects.bulk_create(objects)
      return 'Instancias creadas correctamente'
    except:
      raise ValueError("Hay algo mal en la creacion del historial de compras")
