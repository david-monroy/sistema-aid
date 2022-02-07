from django.http import HttpResponse
import pandas as pd
from backend.models import Pregunta
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def insertarMuestra (request, idEdicion):
    return request


    