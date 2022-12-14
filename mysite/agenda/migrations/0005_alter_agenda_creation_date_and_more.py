# Generated by Django 4.1.3 on 2022-12-06 01:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_alter_agenda_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 1, 31, 0, 985710, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='especialidad',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 1, 31, 0, 956703, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='medico',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 1, 31, 0, 984709, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='medico',
            name='usuario',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='agenda.usuario'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 1, 31, 0, 985710, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 1, 31, 0, 983709, tzinfo=datetime.timezone.utc)),
        ),
    ]
