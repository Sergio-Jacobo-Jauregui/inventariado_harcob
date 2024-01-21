# Generated by Django 5.0.1 on 2024-01-19 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subuser',
            name='type',
            field=models.CharField(blank=True, choices=[('only_read', 'Only_read'), ('read_write', 'Read_write'), ('read_write_delete', 'Read_write_delete')], max_length=50),
        ),
    ]