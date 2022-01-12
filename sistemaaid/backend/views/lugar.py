from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from backend.models import * 
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers.json import DjangoJSONEncoder

@csrf_exempt
def get_municipios(request):

    # estado_id = int(id)

    municipios = modelLugar.Lugar.objects.filter(tipo="MUNICIPIO").values()

    query_respuesta = json.dumps(list(municipios), cls=DjangoJSONEncoder) # Convierte el query retornado en un JSON para enviar a Vue
    return HttpResponse(query_respuesta)

@csrf_exempt
def get_estados(request):

    estados = modelLugar.Lugar.objects.filter(tipo="ESTADO").values()

    query_respuesta = json.dumps(list(estados), cls=DjangoJSONEncoder) # Convierte el query retornado en un JSON para enviar a Vue
    return HttpResponse(query_respuesta)