import pynamodb
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute

import os
from dotenv import load_dotenv
load_dotenv()

class PurchaseRecordModel(Model):
    class Meta:
        table_name = "harcob_inventariado_purchase_records"
        region = os.getenv("AWS_REGION")
        write_capacity_units = 1
        read_capacity_units = 1

    toolNameID = UnicodeAttribute(hash_key=True)
    creationDate = UnicodeAttribute(range_key=True)
    amount = NumberAttribute(null=True)
    amountType = UnicodeAttribute(null=True)
