# Generated by Django 3.2.8 on 2021-11-17 19:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0024_alter_commentmoviemodel_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmoviemodel',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 17, 19, 32, 58, 653477, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
