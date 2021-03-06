# Generated by Django 3.1.3 on 2020-11-17 19:15

import SongsApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('song_name', models.CharField(max_length=100)),
                ('song_description', models.CharField(max_length=125)),
                ('song_cover', models.ImageField(blank=True, null=True, upload_to=SongsApp.models.upload_path)),
            ],
        ),
    ]
