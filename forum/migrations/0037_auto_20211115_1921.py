# Generated by Django 3.2.8 on 2021-11-15 19:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0036_auto_20211115_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 15, 19, 21, 13, 238473, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 15, 19, 21, 13, 237497, tzinfo=utc)),
        ),
    ]
