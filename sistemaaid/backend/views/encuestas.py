from asyncio.windows_events import NULL
from logging import exception
from django.http import HttpResponse
import pandas as pd
from backend.models import Encuesta, Pregunta,Respuesta, PreguntaEdicion,Participante
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers.json import DjangoJSONEncoder

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
        print("Error:"  + err)
        return HttpResponse("Error:"  + err)

