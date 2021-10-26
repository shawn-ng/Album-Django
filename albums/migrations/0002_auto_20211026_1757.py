# Generated by Django 3.2.8 on 2021-10-26 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_alter_artist_members'),
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albums',
            name='artist',
        ),
        migrations.AddField(
            model_name='albums',
            name='album_artist',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='artists.artist'),
        ),
    ]
