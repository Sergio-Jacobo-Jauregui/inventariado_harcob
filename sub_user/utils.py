from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

class AddPermissions:
  def __init__(self, instance, model):
    self.instance = instance
    self.content_type = self.get_content_type(model)
    self.permises = self.recover_permisses()

  def get_content_type(self, model):
    return ContentType.objects.get_for_model(model)

  def recover_permisses(self):
    if self.instance.type == 'only_read':
      return self.give_read_permissions()
    elif self.instance.type == 'read_write':
      return self.give_read_write_permissions()
    elif self.instance.type == 'read_write_delete':
      return self.give_all_permissions()

  def give_read_permissions(self):
    return [ Permission.objects.get_or_create(
              codename="view_permission",
              name='view_permission',
              content_type=self.content_type)[0]
           ]

  def give_read_write_permissions(self):
    permission_set = ['add', 'change']
    permissions = [
      Permission.objects.get_or_create(
        codename=f"{permission}_permission",
        name=f"{permission}_permission",
        content_type=self.content_type
      )[0] for permission in permission_set
    ]

    return self.give_read_permissions() + permissions

  def give_all_permissions(self):
    permission = [
      Permission.objects.get_or_create(
        codename=f"delete_permission",
        name=f"delete_permission",
        content_type=self.content_type
      )[0]
    ]

    return self.give_read_write_permissions() + permission

  def asign_permisses(self):
    self.instance.user_permissions.add(*self.permises)
  
