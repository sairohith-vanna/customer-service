# Generated by Django 3.2.9 on 2021-11-01 14:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=70)),
                ('department_code', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]