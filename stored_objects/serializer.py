import json
# ToDo
class StoredObjectsSerializer:
  def serialize(objects):
    dicc = []
    for object in objects:
      dicc.append({
      'id': object.instance.id,
      'name': object.instance.name,
      'type': object.instance.type,
      'amount': object.instance.amount,
      'organization_id': object.instance.organization_id,
      'work_id': object.instance.work_id,
    })
    return json.dumps(dicc)