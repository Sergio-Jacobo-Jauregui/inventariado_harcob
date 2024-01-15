# Generated by Django 5.0.1 on 2024-01-15 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0004_alter_material_organization_alter_tool_organization'),
        ('organization', '0001_initial'),
        ('usage_record', '0003_alter_usagerecord_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usagerecord',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.organization'),
        ),
        migrations.AlterField(
            model_name='usagerecord',
            name='tool',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='object.tool'),
        ),
    ]
