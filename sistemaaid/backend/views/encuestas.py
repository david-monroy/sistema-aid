import email
from django.http import HttpResponse
import pandas as pd
from backend.models import Encuesta, Pregunta,Respuesta, PreguntaEdicion,Participante,Edicion
from backend.models import * 
from django.contrib.auth.models import User, Group
from backend.serializers import GroupSerializer, UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F,CharField, Value as V
from django.db.models.functions import Concat
from backend.response import *
import math
from django.core.serializers.json import DjangoJSONEncoder
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.core.mail import send_mail
from background_task import background


# @csrf_exempt
# def insertarEncuestas(request,idEdicion):
#     path = request.FILES['file']
#     df = pd.read_excel(path)
#     df = df.to_json()

#     ejecutarInsercion(df, idEdicion)

#     return HttpResponse(response(message="Su petición se realizará en segundo plano, recibirá un correo electrónico cuando termine."))


# @background(schedule=10)
@csrf_exempt
def insertarEncuestas(request,idEdicion,username):
    try:
        path = request.FILES['file']
        df = pd.read_excel(path)
        encuestas = []
        respuestas = []

        getEdicion = Edicion.objects.get(pk=idEdicion)

        for row, column in df.iterrows():
            
            if (math.isnan(column[0]) == False):
                participante = Participante.objects.get(cedula=column[0])
                
                if (column["Sexo_Sexo (F=1 M=2)"] == 1):
                    genero = "M"
                else:
                    genero = "F"

                participante.colegio = modelColegio.Colegio.objects.get(nombre=column["Colegio_Colegio"])
                participante.genero = genero
                participante.save()
                nuevaEncuesta = Encuesta(
                    participante = Participante.objects.get(cedula=column[0]),
                    fechaAplicacion = column[1],
                    codigo = column[2],
                    edicion = getEdicion,
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

        user_email = User.objects.values_list('email', flat=True).filter(username = username)
        user_email = list(user_email)

        send_mail(
            '¡Las encuestas se han cargado!',
            'Se han cargado exitosamente las encuestas que ha subido al Sistema AID',
            'monroy02@gmail.com',
            [user_email[0]],
            fail_silently=False,
        )
        return HttpResponse(response(message="Se insertaron correctamente las " + df.shape[1] + " encuestas"))

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
