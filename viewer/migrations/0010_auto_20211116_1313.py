# Generated by Django 3.2.8 on 2021-11-16 13:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0009_alter_movie_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentmovie',
            options={'ordering': ('publish',)},
        ),
        migrations.RemoveField(
            model_name='commentmovie',
            name='edit',
        ),
        migrations.AddField(
            model_name='commentmovie',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='commentmovie',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='viewer.movie'),
        ),
        migrations.AlterField(
            model_name='commentmovie',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 13, 13, 5, 783800, tzinfo=utc)),
        ),
    ]
