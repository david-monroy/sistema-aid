from django.http import HttpResponse
import pandas as pd
from backend.models import Encuesta, Pregunta,Respuesta, PreguntaEdicion,Participante
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F,CharField, Value as V
from django.db.models.functions import Concat
from backend.response import *
import math


@csrf_exempt
def insertarEncuestas(request,idEdicion):
    try:
        path = request.FILES['file']
        df = pd.read_excel(path)
        encuestas = []
        respuestas = []
        
        for row, column in df.iterrows():
            if (math.isnan(column[0]) == False):
                nuevaEncuesta = Encuesta(
                    participante = Participante.objects.get(cedula=column[0]),
                    fechaAplicacion = column[1],
                    codigo = column[2]
                )
            else: 
                nuevaEncuesta = Encuesta(
                    fechaAplicacion = column[1],
                    codigo = column[2]
                )
           
            encuestas.append(nuevaEncuesta)

            for i in range(3,df.shape[1]):
                codigoPregunta = column.index[i].split('_')[0]
                print(codigoPregunta)
                preguntaEdicion = PreguntaEdicion.objects.get(pregunta__codigo=codigoPregunta, edicion_id=idEdicion)
                if (preguntaEdicion):
                    respuestas.append(Respuesta(
                        respuesta = column[i],
                        encuesta = nuevaEncuesta,
                        pregunta = preguntaEdicion
                    ))
        Encuesta.objects.bulk_create(encuestas)
        Respuesta.objects.bulk_create(respuestas)
    
        return HttpResponse(response(message="Se insertaron correctamente las " + df.shape[1] + " encuestas"))

    except BaseException as err:
        return HttpResponse(error_response(message="Ha ocurrido un error", error=err.args))

@csrf_exempt
def get_encuestas(request,idEdicion):
    try: 
        print(idEdicion)
        encuestas = Encuesta.objects.filter(respuesta__pregunta__edicion__id=idEdicion).distinct()
        encuestasDf = pd.DataFrame(encuestas)

        return HttpResponse(encuestasDf.to_json(orient="table"))             
    except BaseException as err:
        return HttpResponse(err)
