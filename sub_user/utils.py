from django.contrib.auth.models import Permission

class AddPermissions:
  def __init__(self, instance):
    self.instance = instance
    self.models = ['accionrecord', 'organization' ,'purchaserecord' ,'storedobjects' ,'subuser' ,'work' ]
    self.permises = self.recover_permisses()

  def recover_permisses(self):
    if self.instance.type == 'only_read':
      return self.give_read_permissions()
    elif self.instance.type == 'read_write':
      return self.give_read_write_permissions()
    elif self.instance.type == 'read_write_delete':
      return self.give_all_permissions()

  def give_read_permissions(self):
    return  [ 
      Permission.objects.get(codename=f"view_{model}") for model in self.models
    ]

  def give_read_write_permissions(self):
    add_permission = [
      Permission.objects.get(codename=f"add_{model}") for model in self.models 
    ]

    change_permission = [
      Permission.objects.get(codename=f"change_{model}") for model in self.models 
    ]
    return self.give_read_permissions() + add_permission + change_permission

  def give_all_permissions(self):
    delete_permission = [
      Permission.objects.get(codename=f"delete_{model}") for model in self.models 
    ]
    return self.give_read_write_permissions() + delete_permission

  def asign_permisses(self):
    self.instance.user_permissions.add(*self.permises)
  
