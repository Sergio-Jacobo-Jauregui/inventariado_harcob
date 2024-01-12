import pynamodb
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.indexes import LocalSecondaryIndex, AllProjection

import os
from dotenv import load_dotenv
load_dotenv()

class UserDateIndex(LocalSecondaryIndex):
    class Meta:
        index_name = 'useDate-index'
        read_capacity_units = 1
        write_capacity_units = 1
        projection = AllProjection()

    whoUses = UnicodeAttribute(hash_key=True)
    user = UnicodeAttribute(default=0, hash_key=True)

class UsageRecordsModel(Model):
    class Meta:
        table_name = "harcob_inventariado_users"
        region = os.getenv("AWS_REGION")
        write_capacity_units = 1
        read_capacity_units = 1

    whoUses = UnicodeAttribute(hash_key=True)
    toolNameID = UnicodeAttribute(range_key=True)
    useDate = UnicodeAttribute(null=True)
    returnDate = UnicodeAttribute(null=True)
    amount = NumberAttribute(null=True)
    amountType = UnicodeAttribute(null=True)
    local_index_var = UserDateIndex()


    