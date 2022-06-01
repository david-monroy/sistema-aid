from django.db import migrations, models
import django.db.models.deletion


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
                ('codigo', models.IntegerField()),
                ('estaEnUCAB', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Colegio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Edicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('periodo', models.CharField(blank=True, max_length=10, null=True)),
                ('vinculada', models.BooleanField()),
                ('totalMuestra', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('poblacionObjetivo', models.CharField(max_length=50)),
                ('antecedentes', models.CharField(blank=True, max_length=280, null=True)),
                ('objetivoNegocio', models.CharField(max_length=280)),
            ],
        ),
        migrations.CreateModel(
            name='ListaCodigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('descripcion', models.CharField(blank=True, max_length=280, null=True)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaUltimaModificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('fk_lugar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.lugar')),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('genero', models.CharField(blank=True, max_length=1, null=True)),
                ('cedula', models.CharField(max_length=9, unique=True)),
                ('correo', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('correoUcab', models.CharField(blank=True, max_length=50, null=True)),
                ('fechaNacimiento', models.DateField(blank=True, null=True)),
                ('telfPrincipal', models.CharField(max_length=15)),
                ('telfSecundario', models.CharField(blank=True, max_length=15, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, max_length=30, null=True)),
                ('twitter', models.CharField(blank=True, max_length=30, null=True)),
                ('facebook', models.CharField(blank=True, max_length=30, null=True)),
                ('tiktok', models.CharField(blank=True, max_length=30, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30)),
                ('etiqueta', models.CharField(max_length=280)),
                ('tipo', models.CharField(max_length=30)),
                ('listaCodigo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.listacodigo')),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PreguntaEdicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.edicion')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipanteCarrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semestre', models.IntegerField(blank=True, null=True)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.carrera')),
                ('participante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.participante')),
                ('sede', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.sede')),
            ],
        ),
        migrations.AddField(
            model_name='participante',
            name='carreras',
            field=models.ManyToManyField(through='backend.ParticipanteCarrera', to='backend.Carrera'),
        ),
        migrations.AddField(
            model_name='participante',
            name='colegio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.colegio'),
        ),
        migrations.AddField(
            model_name='participante',
            name='lugar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.lugar'),
        ),
        migrations.CreateModel(
            name='MuestraPonderada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeraCondicion', models.CharField(max_length=280)),
                ('segundaCondicion', models.CharField(max_length=280)),
                ('poblacion', models.IntegerField()),
                ('muestra', models.IntegerField()),
                ('edicion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.edicion')),
            ],
        ),
        migrations.CreateModel(
            name='Metodologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcionCualitativa', models.CharField(blank=True, max_length=280, null=True)),
                ('modalidadCualitativa', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcionCuantitativa', models.CharField(blank=True, max_length=280, null=True)),
                ('modalidadCuantitativa', models.CharField(blank=True, max_length=50, null=True)),
                ('edicionId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.edicion')),
            ],
        ),
        migrations.AddField(
            model_name='edicion',
            name='estudio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.estudio'),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=280)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaUltimaModificacion', models.DateTimeField(auto_now=True)),
                ('listaCodigo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.listacodigo')),
            ],
            options={
                'unique_together': {('codigo', 'listaCodigo')},
            },
        ),
        migrations.CreateModel(
            name='Edicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('periodo', models.CharField(blank=True, max_length=10, null=True)),
                ('vinculada', models.BooleanField()),
                ('totalMuestra', models.IntegerField()),
                ('estudio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.estudio')),
            ],
        ),
    ]
