<<<<<<< HEAD
# Generated by Django 3.2.4 on 2021-09-14 15:26
=======
# Generated by Django 3.2.7 on 2021-09-30 20:31
>>>>>>> aid-us1

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('codigo', models.CharField(max_length=20)),
                ('estaEnUCAB', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=1)),
                ('cedula', models.CharField(max_length=9)),
<<<<<<< HEAD
                ('correo', models.CharField(blank=True, max_length=50, null=True)),
=======
>>>>>>> aid-us1
                ('fechaNacimiento', models.DateField(blank=True, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('telfPrincipal', models.CharField(max_length=15)),
                ('telfSecundario', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
    ]
