from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from backend.models import * 
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers.json import DjangoJSONEncoder

@csrf_exempt
def get_participantecarrera(request):

    id = int(request.body)

    participanteCarreras = modelParticipanteCarrera.ParticipanteCarrera.objects.filter(participante_id=id).values()

    query_respuesta = json.dumps(list(participanteCarreras), cls=DjangoJSONEncoder) # Convierte el query retornado en un JSON para enviar a Vue

    return HttpResponse(query_respuesta)