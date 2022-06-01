from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from backend.models import * 
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
<<<<<<< HEAD
from django.core.serializers.json import DjangoJSONEncoder
=======
>>>>>>> 90e4720eda23bb18385e64b04cefeb1a0ccab7a4

@csrf_exempt
def validarCodigo(request):
   requestToDict= json.loads(request.body.decode("utf-8").replace("'", '"'))
   estudio = modelEstudio.Estudio.objects.filter(codigo=requestToDict["codigo"])
<<<<<<< HEAD
   return HttpResponse(estudio)

@csrf_exempt
def obtenerEdiciones(request,id):
    ediciones = modelEdicion.Edicion.objects.filter(estudio_id = id).values()
    query_respuesta = json.dumps(list(ediciones), cls=DjangoJSONEncoder)
    return HttpResponse(query_respuesta)
=======
   return HttpResponse(estudio)
>>>>>>> 90e4720eda23bb18385e64b04cefeb1a0ccab7a4
