# Generated by Django 3.2.8 on 2021-11-12 16:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0033_auto_20211112_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 16, 31, 52, 93987, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 16, 31, 52, 93219, tzinfo=utc)),
        ),
    ]
