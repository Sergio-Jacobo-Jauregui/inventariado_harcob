# Generated by Django 5.0.1 on 2024-01-25 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
        ('person', '0001_initial'),
        ('stored_objects', '0001_initial'),
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccionRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('delivery', 'Delivery'), ('return', 'Return')], max_length=50, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('quantity_type', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='person.person')),
                ('stored_object', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stored_objects.storedobjects')),
                ('work', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='work.work')),
            ],
        ),
    ]
