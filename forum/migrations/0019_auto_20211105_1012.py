# Generated by Django 3.2.8 on 2021-11-05 10:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0018_auto_20211105_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 5, 10, 12, 34, 700783, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 5, 10, 12, 34, 700155, tzinfo=utc)),
        ),
    ]