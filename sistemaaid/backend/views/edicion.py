from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from backend.models import * 
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def validarCodigoEdicion(request):
   requestToDict= json.loads(request.body.decode("utf-8").replace("'", '"'))
   estudio = modelEdicion.Edicion.objects.filter(codigo=requestToDict["codigo"])
   return HttpResponse(estudio)

@csrf_exempt
def tieneEncuestas(request,idEdicion):
    try: 
        print(idEdicion)
        encuestas = Encuesta.objects.filter(respuesta__pregunta__edicion__id=idEdicion)[:1].values()
        
        if (list(encuestas)):
            valor = 1
        else:
            valor = 0

        return HttpResponse(valor)
    except BaseException as err:
        return HttpResponse(err)