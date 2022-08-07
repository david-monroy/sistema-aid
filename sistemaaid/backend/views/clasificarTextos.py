from django.http import HttpResponse
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from backend.ia.clasificarTextos.TextClassifier import train,predict
from backend.models import Encuesta, Respuesta,Categoria
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import F
import os


from backend.serializers import ListaCodigoSerializer

@csrf_exempt
def entrenarModelo(request):
    try:
        path = request.FILES['file']
        df = pd.read_excel(path)
        train(df, "prueba")

        return HttpResponse('Se entrenó el modelo')

    except BaseException as err:
        return HttpResponse(err)

@csrf_exempt
def predecir(request):
    try:
        path = request.FILES['file']
        df = pd.read_excel(path)
        predict(df, "prueba")

        return HttpResponse('Se realizó la predicción del modelo')

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