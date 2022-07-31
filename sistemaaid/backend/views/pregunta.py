from cmath import nan
from xmlrpc.client import ResponseError
from django.http import HttpResponse
import pandas as pd
from backend.models import Pregunta, PreguntaEdicion, Edicion
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import F
import math

from backend.models.modelListaCodigo import ListaCodigo

@csrf_exempt
def previewPreguntas(request):
    path = request.FILES['file']
    df = pd.read_excel(path)
    df['Codigo'] = df['Codigo'].str.replace('_', '-')
    df['Pregunta'] = df['Pregunta'].str.replace('_', ' ')
    return HttpResponse(df.to_json(orient="table"))

@csrf_exempt
def insertarPreguntas(request, idEdicion):
    try:
        path = request.FILES['file']
        df = pd.read_excel(path)
        for row,column in df.iterrows():
            listaCodigo = None
            if (column[2] == 'Cadena'):
                if (math.isnan(column[3]) == True):
                    return HttpResponse("Debe asociar una lista de código a la pregunta " + column [0])
                else:
                    listaCodigo = asignarListaCodigo(column[3])
            preguntaFilter = Pregunta.objects.filter(preguntaedicion__edicion=idEdicion, codigo=column[0])
            if (preguntaFilter):
                pregunta = Pregunta.objects.get(preguntaedicion__edicion=idEdicion, codigo=column[0])
                pregunta.etiqueta = column[1]
                pregunta.tipo = column[2]
                if (listaCodigo != None):
                    pregunta.listaCodigo = listaCodigo
                pregunta.save()
            else:
                if (listaCodigo != None):
                    
                    nueva_pregunta = Pregunta.objects.create(
                        codigo = column[0],
                        etiqueta = column[1],
                        tipo= column[2],
                        listaCodigo = listaCodigo   
                    )
                else:

                    nueva_pregunta = Pregunta.objects.create(
                        codigo = column[0],
                        etiqueta = column[1],
                        tipo= column[2] 
                    )

                PreguntaEdicion.objects.create(
                    pregunta = nueva_pregunta,
                    edicion = Edicion.objects.get(pk=idEdicion)
                )
        return HttpResponse("Se cargó exitosamente el instrumento")
    except BaseException as err:
        return HttpResponse(err)

def asignarListaCodigo(id):
    listaCodigo = None
    if (ListaCodigo.objects.filter(pk=id)):
        listaCodigo = ListaCodigo.objects.get(pk=id)
    return listaCodigo

@csrf_exempt
def get_preguntas(request,idEdicion):
    try: 
        preguntas = Pregunta.objects.filter(preguntaedicion__edicion=idEdicion).values(
                                    'id','etiqueta','codigo','tipo').annotate(
                                        listaCodigo=F('listaCodigo__nombre'))
        query_respuesta = json.dumps(list(preguntas), cls=DjangoJSONEncoder) 
        return HttpResponse(query_respuesta)
    except BaseException as err:
        return HttpResponse(err)





    


    