# Generated by Django 3.2.12 on 2022-04-09 00:56

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='travel',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
