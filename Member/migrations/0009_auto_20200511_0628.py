# Generated by Django 3.0.6 on 2020-05-11 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0008_auto_20200511_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='session',
            field=models.CharField(max_length=50),
        ),
    ]
