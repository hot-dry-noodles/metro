# Generated by Django 3.0 on 2019-12-05 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20191205_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbor',
            old_name='prev_station',
            new_name='prev_station_id',
        ),
    ]
