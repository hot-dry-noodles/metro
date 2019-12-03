# Generated by Django 2.2.7 on 2019-12-03 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='booking.Line')),
                ('next', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='next', to='booking.Terminal')),
                ('prev', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='prev', to='booking.Terminal')),
                ('terminal', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='terminal', to='booking.Terminal')),
            ],
        ),
    ]