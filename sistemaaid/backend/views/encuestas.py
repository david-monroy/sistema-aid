from django.http import HttpResponse
import pandas as pd
from backend.models import Encuesta, Pregunta,Respuesta, PreguntaEdicion,Participante
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F,CharField, Value as V
from django.db.models.functions import Concat
from backend.errorResponse import error_response
import json
from rest_framework import status


@csrf_exempt
def insertarEncuestas(request,idEdicion):
    try:
        path = request.FILES['file']
        df = pd.read_excel(path)

        for row, column in df.iterrows():
            
            if (Participante.objects.filter(cedula=column[0])):
                nuevaEncuesta = Encuesta.objects.create(
                    participante = column[0],
                    fechaAplicacion = column[1],
                    codigo = column[2]
                )
            else: 
                nuevaEncuesta = Encuesta.objects.create(
                    fechaAplicacion = column[1],
                    codigo = column[2]
                )
           
            for i in range(3,df.shape[1]):
                codigoPregunta = column.index[i].split('_')[0]
                print(codigoPregunta)
                pregunta = Pregunta.objects.get(preguntaedicion__edicion=idEdicion, codigo=codigoPregunta)
                preguntaEdicion = PreguntaEdicion.objects.get(pregunta_id= pregunta.id)
                if (pregunta):
                    nuevaRespuesta = Respuesta.objects.create(
                        respuesta = column[i],
                        encuesta = nuevaEncuesta,
                        pregunta = preguntaEdicion
                    )
    
        return HttpResponse('Se inserto correctamente')

    except BaseException as err:
        return HttpResponse(error_response(message="Ha ocurrido un error", error=err.args, status=status.HTTP_400_BAD_REQUEST))

@csrf_exempt
def get_encuestas(request,idEdicion):
    try: 
        encuestas = Encuesta.objects.filter(respuesta__pregunta__edicion=idEdicion).values(
                                    'codigo','fechaAplicacion', 'respuesta__respuesta', 'respuesta__pregunta__pregunta__codigo').annotate(
                                        participante=F('participante__nombre'))
        preguntas = Pregunta.objects.filter(preguntaedicion__edicion=idEdicion).values('codigo','etiqueta').annotate(pregunta=Concat('codigo', V('_'),'etiqueta'))
        preguntasDf = pd.DataFrame(preguntas)
        preguntasDf = preguntasDf.drop(['codigo', 'etiqueta'], axis=1)
        respuestasDf = pd.DataFrame(encuestas)
        encuestasDf = pd.DataFrame()
        encuestasDf['ID'] = respuestasDf['codigo']
        encuestasDf['Fecha de Aplicacion'] = respuestasDf['fechaAplicacion']
        encuestasDf['Participante']=respuestasDf['participante']
        for row,column in preguntasDf.iterrows():
            nombreColumna = column[0]
            encuestasDf[nombreColumna] = ""

        for row1,column1 in encuestasDf.iterrows():
            for row2,column2 in respuestasDf.iterrows():
                for i in range(3,encuestasDf.shape[1]):
                    if(column2[3]==column1.index[i].split('_')[0]):
                        if(column2[0]==column1[0]):
                            encuestasDf.loc[row1, column1.index[i]]=column2[2]

        return HttpResponse(encuestasDf.to_json(orient="table"))             
    except BaseException as err:
        return HttpResponse(err)
