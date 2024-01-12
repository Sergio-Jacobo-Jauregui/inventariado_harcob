import pynamodb
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute

import os
from dotenv import load_dotenv
load_dotenv()

class UserModel(Model):
    class Meta:
        table_name = "harcob_inventariado_users"
        region = os.getenv("AWS_REGION")
        write_capacity_units = 1
        read_capacity_units = 1

    userID = NumberAttribute(hash_key=True)
    username = UnicodeAttribute(null=True)
    password = UnicodeAttribute(null=True)