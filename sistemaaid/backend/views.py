from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from . import models
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def leer_csv(request):

    path = request.FILES['file']

    df = pd.read_csv(path, header=0, encoding='ISO-8859-1', delimiter=',')
    
    row_iter = df.iterrows()

    df['Fecha nacimiento'] = pd.to_datetime(df['Fecha nacimiento'])

    df = df.replace('nan','nulo')

    for index, row in row_iter:
        nuevo_participante = models.Participante.objects.create(
            nombre = row[0],
            cedula  = row[1],
            genero = row[2],
            telfPrincipal = row[3],
            telfSecundario = row[4],
            correo = row[5],
            fechaNacimiento = row[6],
            edad = row[7],
            colegio = models.Colegio.objects.get(pk=row[8]),
        )

        nuevo_participante_carrera = models.ParticipanteCarrera.objects.create(
            participante = nuevo_participante,
            sede  = models.Sede.objects.get(pk=row[9]),
            carrera = models.Carrera.objects.get(pk=row[10]),
            semestre = row[11],
        )

    return HttpResponse(df)

@csrf_exempt
def leer_csv_actualizar(request):

    path = request.FILES['file']

    df = pd.read_csv(path, header=0, encoding='ISO-8859-1', delimiter=';')
    
    row_iter = df.iterrows()

    for index, row in row_iter:
        par = models.Participante.objects.get(cedula=row[1])

        if (par):
            par.nombre = row[0]
            par.genero = row[2]
            par.telfPrincipal = row[3]
            par.telfSecundario = row[4]
            par.correo = row[5]
            par.edad = row[7]
            print(par.edad)
            print(par.telfPrincipal)
            print(par.correo)
        #     # par.colegio = models.Colegio.objects.get(pk=row[8]),
            par.save()

        # par_car = models.ParticipanteCarrera.objects.get(participante=par.id)
        # if (par_car):
        #     par_car.sede  = models.Sede.objects.get(pk=row[9]),
        #     par_car.carrera = models.Carrera.objects.get(pk=row[10]),
        #     par_car.semestre = row[11],
        #     par_car.save

    return HttpResponse(df)
