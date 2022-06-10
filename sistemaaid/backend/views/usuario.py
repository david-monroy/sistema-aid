from datetime import date, datetime, timedelta
from email.headerregistry import Group
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from backend.models import * 
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User, Group
from backend.serializers import GroupSerializer, UserSerializer
from rest_framework.decorators import action

# Create your views here.
@csrf_exempt
def agregar_usuario(request):

    usuario_dict = json.loads(request.body.decode('utf8').replace("'", '"')) # request en formato DICCIONARIO, esto servira para trabajar los atributos en DJango
        
    user = User.objects.create_user(usuario_dict["username"], usuario_dict['email'], usuario_dict["password"])

    user.first_name = usuario_dict["first_name"]
    user.last_name = usuario_dict["last_name"]
    user.save()
    user.groups.add(usuario_dict["group"])
    

    return HttpResponse(user)

@csrf_exempt
def obtener_usuarios(request):

    queryset = User.objects.all()
    serializers = UserSerializer(queryset, many=True)
    usuariosJSON = json.dumps(serializers.data, cls=DjangoJSONEncoder) 
    return HttpResponse(usuariosJSON)

@csrf_exempt
def obtener_usuario(request):
        requestToDict= json.loads(request.body.decode("utf-8").replace("'", '"'))
        queryset = User.objects.filter(username = requestToDict["username"])
        serializers = UserSerializer(queryset, many=True)
        usuariosJSON = json.dumps(serializers.data, cls=DjangoJSONEncoder)
        return HttpResponse(usuariosJSON)

@csrf_exempt
def obtener_usuario_id(request, id):
        queryset = User.objects.get(pk = id)
        query_respuesta = json.dumps(queryset, cls=DjangoJSONEncoder)
        return HttpResponse(query_respuesta)

@csrf_exempt
def editar_usuario(request, id):
        queryset = User.objects.get(pk = id)
        queryset.delete()
        return HttpResponse("Exitoso")
