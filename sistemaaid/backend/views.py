from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from . import models
from django.conf import settings

# Create your views here.
def leer_csv(request):
    path = r'C:\Users\djmon\Documents\TESIS\sistema-aid\sistemaaid\backend\participantes.csv'
    df = pd.read_csv(path, header=0, encoding='ISO-8859-1', delimiter=',')
    
    row_iter = df.iterrows()

    objs = [

        models.Participante(
            nombre = row[0],
            cedula  = row[1],
            genero = row[2],
            telfPrincipal = row[3]
        )

        for index, row in row_iter

    ]

    models.Participante.objects.bulk_create(objs)
    print(df.columns)

    return HttpResponse(df)