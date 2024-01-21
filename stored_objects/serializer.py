import json

class StoredObjectsSerializer:
  def serialize(objects):
    dicc = []
    for object in objects:
      dicc.append({
      'id': object.id,
      'name': object.name,
      'type': object.type,
      'amount': object.amount,
      'organization_id': object.organization_id,
      'work_id': object.work_id,
    })
    return json.dumps(dicc)
