from datetime import date, datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from backend.models import * 
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User

# Create your views here.
@csrf_exempt
def agregar_usuario(request):

    usuario_dict = json.loads(request.body.decode('utf8').replace("'", '"')) # request en formato DICCIONARIO, esto servira para trabajar los atributos en DJango
        
    user = User.objects.create_user(usuario_dict["username"], usuario_dict['email'], usuario_dict["password"])

    user.first_name = usuario_dict["first_name"]
    user.last_name = usuario_dict["last_name"]
    user.save()

    return HttpResponse(user)

@csrf_exempt
def obtener_usuarios(request):

    usuarios = User.objects.filter().values()
    usuariosJSON = json.dumps(list(usuarios), cls=DjangoJSONEncoder) # Convierte el query retornado en un JSON para enviar a Vue
    print(usuariosJSON)

    return HttpResponse(usuariosJSON)