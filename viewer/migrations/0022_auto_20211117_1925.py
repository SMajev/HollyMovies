# Generated by Django 3.2.8 on 2021-11-17 19:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0021_alter_commentmoviemodel_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default='elooo', max_length=250, unique_for_date='publish'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commentmoviemodel',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 17, 19, 25, 7, 367995, tzinfo=utc)),
        ),
    ]
