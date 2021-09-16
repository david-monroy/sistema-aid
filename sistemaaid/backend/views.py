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

    objs = [
        models.Participante(
            nombre = row[0],
            cedula  = row[1],
            genero = row[2],
            telfPrincipal = row[3],
            telfSecundario = row[4],
            correo = row[5],
            fechaNacimiento = row[6],
            edad = row[7],
            colegio = row[8],
            sede = row[9],
            carrera = row[10],
            semestre = row[11],
        )
        for index, row in row_iter
    ]

    models.Participante.objects.bulk_create(objs)
    models.ParticipanteCarrera.objects.bulk_create(objs)

    return HttpResponse(df)
