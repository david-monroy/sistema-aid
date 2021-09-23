from datetime import date, datetime, timedelta
from dateutil import relativedelta
import dateutil
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from backend.models import * 
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction

# Create your views here.
@csrf_exempt
def leer_csv(request):

    path = request.FILES['file']

    df = pd.read_csv(path, header=0, encoding='ISO-8859-1', delimiter=';')
    
    row_iter = df.iterrows()

    df['Fecha nacimiento'] = pd.to_datetime(df['Fecha nacimiento'])
    df['Telefono secundario']=df['Telefono secundario'].fillna('')
    df['Correo ucab']=df['Correo ucab'].fillna('')
    
    for index, row in row_iter:

            nuevo_participante = modelParticipante.Participante.objects.create(
                nombre = row[0],
                cedula  = row[1],
                genero = row[2],
                telfPrincipal = row[3],
                telfSecundario = row[4],
                correo = row[5],
                correoUcab = row[6],
                fechaNacimiento = row[7],
                colegio = modelColegio.Colegio.objects.get(pk=row[8]),
            )

            nuevo_participante_carrera = modelParticipanteCarrera.ParticipanteCarrera.objects.create(
                participante = nuevo_participante,
                sede  = modelSede.Sede.objects.get(pk=row[9]),
                carrera = modelCarrera.Carrera.objects.get(pk=row[10]),
                semestre = row[11],
            )

    return HttpResponse(df)

@csrf_exempt
def leer_csv_actualizar(request):

    path = request.FILES['file']

    df = pd.read_csv(path, header=0, encoding='ISO-8859-1', delimiter=';')
    
    row_iter = df.iterrows()

    for index, row in row_iter:
        existe_participante = modelParticipante.Participante.objects.filter(cedula=row[1])

        if (existe_participante):
            par = modelParticipante.Participante.objects.get(cedula=row[1])
            par.nombre = row[0]
            par.genero = row[2]
            par.telfPrincipal = row[3]
            par.telfSecundario = row[4]
            par.correo = row[5]
            par.edad = row[7]
            par.colegio = modelColegio.Colegio.objects.get(pk=row[8])
            par.save()

            existe_par_car = modelParticipanteCarrera.ParticipanteCarrera.objects.filter(participante=par.id)

            if (existe_par_car):
                par_car = modelParticipanteCarrera.ParticipanteCarrera.objects.get(participante=par.id)
                par_car.sede  = modelSede.Sede.objects.get(pk=row[9])
                par_car.carrera = modelCarrera.Carrera.objects.get(pk=row[10])
                par_car.semestre = row[11]
                par_car.save()
        else:
            print('no existe')

    return HttpResponse(df)
