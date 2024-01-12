import pynamodb
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection

import os
from dotenv import load_dotenv
load_dotenv()

class UserIndex(GlobalSecondaryIndex):
    class Meta:
        index_name = 'userID-index'
        read_capacity_units = 1
        write_capacity_units = 1
        projection = AllProjection()

    user = NumberAttribute(default=0, hash_key=True)

class ToolModel(Model):
    class Meta:
        table_name = "harcob_inventariado_tools"
        region = os.getenv("AWS_REGION")
        write_capacity_units = 1
        read_capacity_units = 1

    toolNameID = UnicodeAttribute(hash_key=True)
    size = UnicodeAttribute(null=True)
    type = UnicodeAttribute(null=True)
    global_index_var = UserIndex()
