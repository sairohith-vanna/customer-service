from django.db import models
import uuid
import datetime

from departments.models import Department

class Representative(models.Model):

    representative_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    representative_name = models.CharField(max_length=100)
    is_active_working = models.BooleanField(default=True)
    start_date = models.DateField(default=datetime.date.today)

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True
    )
