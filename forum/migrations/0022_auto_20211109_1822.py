# Generated by Django 3.2.8 on 2021-11-09 18:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0021_auto_20211109_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 18, 22, 53, 237992, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 18, 22, 53, 237313, tzinfo=utc)),
        ),
    ]
