# Generated by Django 2.1.7 on 2022-10-11 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20221011_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 10, 11, 10, 52, 24, 482052)),
        ),
    ]
