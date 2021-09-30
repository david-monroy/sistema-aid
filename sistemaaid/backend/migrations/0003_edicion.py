# Generated by Django 3.2.7 on 2021-09-30 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210929_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('periodo', models.CharField(max_length=10)),
                ('vinculada', models.BooleanField()),
                ('TotalMuestra', models.IntegerField()),
            ],
        ),
    ]
