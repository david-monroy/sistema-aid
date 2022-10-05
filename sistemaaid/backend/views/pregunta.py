from cmath import nan
from xmlrpc.client import ResponseError
from django.http import HttpResponse
import pandas as pd
from backend.models import Pregunta, PreguntaEdicion, Edicion
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers.json import DjangoJSONEncoder
import math
from django.db.models import F, Value as V
from django.db.models.functions import Concat
from backend.response import *
from tkinter.filedialog import asksaveasfilename

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
        data = request.body.decode('utf8').replace("'", '"')
        df = pd.DataFrame(json.loads(data))
        for row,column in df.iterrows():
            listaCodigo = None
            if (column[3] == 'Cadena'):
                if (math.isnan(column[4]) == False):
                    listaCodigo = asignarListaCodigo(column[4])
     
            preguntaFilter = Pregunta.objects.filter(codigo=column[1])
            if (preguntaFilter):
                pregunta = Pregunta.objects.get(codigo=column[1])
                pregunta.etiqueta = column[2]
                pregunta.tipo = column[3]
                if (listaCodigo != None):
                    pregunta.listaCodigo = listaCodigo
                pregunta.save()

                preguntaParaEstaEdicion = Pregunta.objects.filter(preguntaedicion__edicion=idEdicion, codigo=column[1])
                if (preguntaParaEstaEdicion):
                    pass
                else:
                    PreguntaEdicion.objects.create(
                    pregunta = pregunta,
                    edicion = Edicion.objects.get(pk=idEdicion)
                    )
            else:
                if (listaCodigo != None):
                    nueva_pregunta = Pregunta.objects.create(
                        codigo = column[1],
                        etiqueta = column[2],
                        tipo= column[3],
                        listaCodigo = listaCodigo   
                    )
                else:
                    nueva_pregunta = Pregunta.objects.create(
                        codigo = column[1],
                        etiqueta = column[2],
                        tipo= column[3] 
                    )

                PreguntaEdicion.objects.create(
                    pregunta = nueva_pregunta,
                    edicion = Edicion.objects.get(pk=idEdicion)
                )

        return HttpResponse(response(message="Se cargó exitosamente el instrumento"))
    except BaseException as err:
        return HttpResponse(error_response(message="Ha ocurrido un error", error=err.args))

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

@csrf_exempt
def get_preguntasPorEdiciones(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        preguntas = Pregunta.objects.filter(preguntaedicion__edicion__pk__in=data).values('id','etiqueta').distinct()
        query_respuesta = json.dumps(list(preguntas), cls=DjangoJSONEncoder) 
        return HttpResponse(query_respuesta)
    except BaseException as err:
        return HttpResponse(err)

@csrf_exempt
def get_dataEntry(request,idEdicion):
    try: 
        preguntas = Pregunta.objects.filter(preguntaedicion__edicion=idEdicion).values('codigo','etiqueta').annotate(pregunta=Concat('codigo', V('_'),'etiqueta'))
        preguntasDf = pd.DataFrame(preguntas)
        preguntasDf = preguntasDf.drop(['codigo', 'etiqueta'], axis=1)
        preguntasDf = preguntasDf.set_index('pregunta').T
        preguntasDf.insert(0,"Participante","")
        preguntasDf.insert(1,"Fecha","")
        preguntasDf.insert(2,"ID","")
        file_name = asksaveasfilename(filetypes=[('excel file', '*.xlsx')], defaultextension='.xlsx')
        preguntasDf.to_excel(file_name)
        return HttpResponse(preguntasDf.to_json(orient="table"))             
    except BaseException as err:
        return HttpResponse(err)


    


    