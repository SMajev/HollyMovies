# Generated by Django 3.2.8 on 2021-11-09 20:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0025_auto_20211109_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 20, 45, 34, 737039, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 20, 45, 34, 736318, tzinfo=utc)),
        ),
    ]