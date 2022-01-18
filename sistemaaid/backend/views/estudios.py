from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from backend.models import * 
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def validarCodigo(request):
   requestToDict= json.loads(request.body.decode("utf-8").replace("'", '"'))
   estudio = modelEstudio.Estudio.objects.filter(codigo=requestToDict["codigo"])
   return HttpResponse(estudio)