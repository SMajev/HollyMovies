# Generated by Django 3.2.8 on 2021-11-12 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0006_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.FileField(default='download.jpg', upload_to='./covers'),
        ),
    ]
