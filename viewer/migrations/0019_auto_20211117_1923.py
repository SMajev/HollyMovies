# Generated by Django 3.2.8 on 2021-11-17 19:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0018_alter_commentmoviemodel_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='slug',
        ),
        migrations.AlterField(
            model_name='commentmoviemodel',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 17, 19, 23, 35, 406296, tzinfo=utc)),
        ),
    ]