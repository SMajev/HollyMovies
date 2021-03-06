# Generated by Django 3.2.8 on 2021-11-16 13:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('viewer', '0011_alter_commentmovie_publish'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentMovieModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=datetime.datetime(2021, 11, 16, 13, 46, 47, 271160, tzinfo=utc))),
                ('update', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='viewer.movie')),
            ],
            options={
                'ordering': ('publish',),
            },
        ),
        migrations.DeleteModel(
            name='CommentMovie',
        ),
    ]
