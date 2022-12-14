# Generated by Django 4.1.3 on 2022-12-05 23:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2022, 12, 5, 23, 24, 25, 757334, tzinfo=datetime.timezone.utc))),
                ('level', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='agenda',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='agenda',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 5, 23, 24, 25, 759334, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='especialidad',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 5, 23, 24, 25, 728327, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='medico',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 5, 23, 24, 25, 757334, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='paciente',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 5, 23, 24, 25, 758334, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='medico',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='agenda.usuario'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='agenda.usuario'),
        ),
    ]
