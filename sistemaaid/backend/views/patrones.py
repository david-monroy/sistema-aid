from django.http import HttpResponse
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from backend.ia.patrones.randomForestClassifier import entrenar, exportarArbol
from backend.models import Respuesta,Categoria
from django.db.models import F
import os
from backend.response import *
from django.http import HttpResponse
from random import random
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split
from PIL import Image, ImageDraw, ImageFont
from subprocess import check_call
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn import tree
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import pickle
from tkinter.filedialog import asksaveasfilename


@csrf_exempt
def entrenarArbol(request):
    try:
        path = request.FILES['file']
        df = pd.read_excel(path)
        ##df = df.dropna(axis=1, how='all', inplace=False)
        ##df =df.replace(-777777777,)
        ##df =df.replace(-999999999,)
        ##for i in range(0,df.shape[1]):
        ##    clasificacion = pd.get_dummies(df.iloc[:,i], prefix=df.columns[i])
        ##    df= df.join(clasificacion)

        ##df = df.drop(df.iloc[:, 0:i],axis = 1)
        entrenar(df)
        return HttpResponse(response(message="Se preproceso todo correctamente"))

    except BaseException as err:
        return HttpResponse(err)

@csrf_exempt
def exportar(request):
    try:
        print("entra")
        exportarArbol()
        return HttpResponse(response(message="Se exportó uno de los árboles"))

    except BaseException as err:
        return HttpResponse(err)

@csrf_exempt
def clasificar(request,idEdicion):
    try:
        respuestas = []
        listasCodigo = Respuesta.objects.filter(
                                encuesta__estaCodificada=False,
                                pregunta__edicion_id = idEdicion,
                                pregunta__pregunta__tipo="Cadena").values('pregunta__pregunta__listaCodigo__nombre','pregunta__pregunta__listaCodigo__id'
                                                                ).distinct().annotate(
                                                                                nombre=F('pregunta__pregunta__listaCodigo__nombre'),
                                                                                id = F('pregunta__pregunta__listaCodigo__id')
                                                                                ).order_by('pregunta__pregunta__listaCodigo__id')
        for lista in listasCodigo:
            if (os.path.exists("backend/ia/clasificarTextos/"+ lista["nombre"])):
                respuestasACodificar = Respuesta.objects.filter(
                                    encuesta__estaCodificada=False,
                                    pregunta__edicion_id = idEdicion,
                                    pregunta__pregunta__tipo="Cadena",
                                    pregunta__pregunta__listaCodigo__id=lista["id"]
                                    ).values('id','respuesta','codigo','encuesta_id'
                                    ).annotate(listaCodigo=F('pregunta__pregunta__listaCodigo__nombre'),
                                                listaCodigoId = F('pregunta__pregunta__listaCodigo__id'),
                                                preguntaId = F('pregunta__pregunta')).order_by('pregunta__pregunta__listaCodigo__id')
        
                df = pd.DataFrame(respuestasACodificar)
                df = predict(df, lista["nombre"])
                for row,column in df.iterrows():
                    if column[7]=="nan":
                        codigo = "nan"
                    else:
                        categoria = Categoria.objects.get(listaCodigo=column[5], descripcion=column[7])
                        codigo = categoria.codigo

                    respuesta = Respuesta.objects.get(pk=column[0])
                    respuesta.codigo = codigo
                    respuesta.save()
        return HttpResponse("Se realizó la predicción")

    except BaseException as err:
        return HttpResponse(err)