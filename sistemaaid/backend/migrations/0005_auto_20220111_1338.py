# Generated by Django 3.2.4 on 2022-01-11 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_lugar_prueba'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lugar',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='lugar',
            name='prueba',
        ),
    ]