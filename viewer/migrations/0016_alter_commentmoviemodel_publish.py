# Generated by Django 3.2.8 on 2021-11-17 19:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0015_auto_20211117_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmoviemodel',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 17, 19, 20, 13, 644143, tzinfo=utc)),
        ),
    ]
