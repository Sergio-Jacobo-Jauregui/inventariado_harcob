# Generated by Django 5.0.1 on 2024-01-15 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0001_initial'),
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='work.work'),
        ),
        migrations.AddField(
            model_name='tool',
            name='work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='work.work'),
        ),
    ]