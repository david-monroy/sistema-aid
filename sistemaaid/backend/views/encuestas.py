from django.http import HttpResponse
import pandas as pd
from backend.models import Encuesta, Pregunta,Respuesta, PreguntaEdicion,Participante,Edicion
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

        getEdicion = Edicion.objects.get(pk=idEdicion)
        
        for row, column in df.iterrows():
            
            if (math.isnan(column[0]) == False):
                nuevaEncuesta = Encuesta(
                    participante = Participante.objects.get(cedula=column[0]),
                    fechaAplicacion = column[1],
                    codigo = column[2],
                    edicion = getEdicion
                )
            else: 
                nuevaEncuesta = Encuesta(
                    fechaAplicacion = column[1],
                    codigo = column[2],
                    edicion = getEdicion
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
    
        return HttpResponse(response(message="Se insertaron correctamente las " + str(df.shape[1]) + " encuestas"))

    except BaseException as err:
        return HttpResponse(error_response(message="Ha ocurrido un error", error=err.args))

@csrf_exempt
def get_encuestas(request,idEdicion):
    try: 
        encuestas = Encuesta.objects.filter(edicion=idEdicion).values('codigo', 'fechaAplicacion').annotate(
                                        participante=F('participante__nombre'))
        encuestasDf = pd.DataFrame(encuestas)

        preguntas = Pregunta.objects.filter(preguntaedicion__edicion=idEdicion).values('codigo','etiqueta').annotate(pregunta=Concat('codigo', V('_'),'etiqueta'))
        preguntasDf = pd.DataFrame(preguntas)
        preguntasDf = preguntasDf.drop(['codigo', 'etiqueta'], axis=1)
        preguntasDf = preguntasDf.set_index('pregunta').T
        encuestasDf = pd.concat((encuestasDf,preguntasDf),axis=0)


        respuestas = Respuesta.objects.filter(encuesta__edicion=idEdicion).values('respuesta', 'pregunta__pregunta__codigo', 'encuesta_id')
        respuestasDf= pd.DataFrame(respuestas)

        for row1,column1 in encuestasDf.iterrows():
            for row2,column2 in respuestasDf.iterrows():
                for i in range(3,encuestasDf.shape[1]):
                    if(column2[1]==column1.index[i].split('_')[0]):
                        if(column2[2]==column1[0]):
                            encuestasDf.loc[row1, column1.index[i]]=column2[0]

        return HttpResponse(respuestasDf.to_json(orient="table"))             
    except BaseException as err:
        return HttpResponse(err)
