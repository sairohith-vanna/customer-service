# Generated by Django 3.2.8 on 2021-11-01 11:22

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Representative',
            fields=[
                ('representative_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('representative_name', models.CharField(max_length=100)),
                ('is_active_working', models.BooleanField(default=True)),
                ('start_date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
