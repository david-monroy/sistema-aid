from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from backend.models import * 
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_participantecarrera(request):

    print(request)
    participanteCarreras = modelParticipante.Participante.objects.filter(id=request.id)
    print(participanteCarreras)

    return participanteCarreras