from django.db import models
from django.db.models.fields import BooleanField, CharField, UUIDField
import uuid

class Department(models.Model):

    department_id = UUIDField(default=uuid.uuid4, primary_key=True,editable=False)
    department_name = CharField(max_length=70, null=False)
    department_code = CharField(max_length=10, null=False)
    is_active = BooleanField(default=True)
