# Generated by Django 5.0.1 on 2024-01-23 21:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accion_record', '0003_accionrecord_dni'),
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accionrecord',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='accionrecord',
            name='person_name',
        ),
        migrations.AddField(
            model_name='accionrecord',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='person.person'),
        ),
        migrations.AlterField(
            model_name='accionrecord',
            name='type',
            field=models.CharField(choices=[('delivery', 'Delivery'), ('return', 'Return')], max_length=50, null=True),
        ),
    ]
