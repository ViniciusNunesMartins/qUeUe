# Generated by Django 3.0.6 on 2020-05-11 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Queue', '0003_auto_20200509_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='establishment_closetime',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
    ]