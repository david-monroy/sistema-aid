# Generated by Django 3.2.7 on 2021-10-06 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudio',
            name='objetivoOrganizacion',
        ),
    ]
