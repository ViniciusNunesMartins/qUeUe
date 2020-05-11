# Generated by Django 3.0.6 on 2020-05-10 03:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0005_auto_20200510_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='session',
            field=models.UUIDField(default=uuid.uuid5, unique=True),
        ),
    ]