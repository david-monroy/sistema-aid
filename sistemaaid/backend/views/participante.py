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

# Create your views here.
@csrf_exempt
def agregar_masivo(request):

    path = request.FILES['file']

    df = pd.read_csv(path, header=0, encoding='ISO-8859-1', delimiter=';')
    
    row_iter = df.iterrows()

    df['Fecha de nacimiento'] = pd.to_datetime(df['Fecha de nacimiento'])
    df['Telf. Secundario']=df['Telf. Secundario'].fillna('')
    df['Correo UCAB']=df['Correo UCAB'].fillna('')
    df['Municipio']=df['Municipio'].fillna('')
    lugar = ''
    estado = ''
    
    for index, row in row_iter:

            if (row[9]):
                estado = modelLugar.Lugar.objects.filter(nombre=row[8], tipo = 'ESTADO').values('id').distinct()
                for l in list(estado):
                    print(type(l))
                    lugar = modelLugar.Lugar.objects.get(nombre=row[9], fk_lugar = int(l['id']))
                    
            else:
                lugar = modelLugar.Lugar.objects.get(nombre=row[8], tipo = 'ESTADO')
            
            nuevo_participante = modelParticipante.Participante.objects.create(
                nombre = row[0],
                cedula  = row[1],
                genero = row[2],
                telfPrincipal = row[3],
                telfSecundario = row[4],
                correo = row[5],
                correoUcab = row[6],
                fechaNacimiento = row[7],
                lugar = lugar,
                direccion = row[10],
                colegio = modelColegio.Colegio.objects.get(nombre=row[11]),
                instagram = row[15],
                twitter = row[16],
                facebook = row[17],
                tiktok = row[18],
                linkedin = row[19],
            )

            nuevo_participante_carrera = modelParticipanteCarrera.ParticipanteCarrera.objects.create(
                participante = nuevo_participante,
                sede  = modelSede.Sede.objects.get(nombre=row[12]),
                carrera = modelCarrera.Carrera.objects.get(nombre=row[13]),
                semestre = row[14],
            )

    return HttpResponse(df)

@csrf_exempt
def editar_masivo(request):

    path = request.FILES['file']

    df = pd.read_csv(path, header=0, encoding='ISO-8859-1', delimiter=';')
    
    row_iter = df.iterrows()

    df['Fecha nacimiento'] = pd.to_datetime(df['Fecha nacimiento'])
    df['Telefono secundario']=df['Telefono secundario'].fillna('')
    df['Correo ucab']=df['Correo ucab'].fillna('')

    for index, row in row_iter:
        existe_participante = modelParticipante.Participante.objects.filter(cedula=row[1])

        if (existe_participante):
            par = modelParticipante.Participante.objects.get(cedula=row[1])
            par.nombre = row[0]
            par.genero = row[2]
            par.telfPrincipal = row[3]
            par.telfSecundario = row[4]
            par.correo = row[5]
            par.correoUcab = row[6]
            par.colegio = modelColegio.Colegio.objects.get(pk=row[8])
            par.save()

            existe_par_car = modelParticipanteCarrera.ParticipanteCarrera.objects.filter(participante=par.id)

            if (existe_par_car):
                par_car = modelParticipanteCarrera.ParticipanteCarrera.objects.get(participante=par.id)
                par_car.sede  = modelSede.Sede.objects.get(pk=row[9])
                par_car.carrera = modelCarrera.Carrera.objects.get(pk=row[10])
                par_car.semestre = row[11]
                par_car.save()
        else:
            nuevo_participante = modelParticipante.Participante.objects.create(
                nombre = row[0],
                cedula  = row[1],
                genero = row[2],
                telfPrincipal = row[3],
                telfSecundario = row[4],
                correo = row[5],
                correoUcab = row[6],
                fechaNacimiento = row[7],
                colegio = modelColegio.Colegio.objects.get(pk=row[8]),
                instagram = row[12],
                twitter = row[13],
                facebook = row[14],
                tiktok = row[15],
                linkedin = row[16],
            )

            nuevo_participante_carrera = modelParticipanteCarrera.ParticipanteCarrera.objects.create(
                participante = nuevo_participante,
                sede  = modelSede.Sede.objects.get(pk=row[9]),
                carrera = modelCarrera.Carrera.objects.get(pk=row[10]),
                semestre = row[11],
            )

    return HttpResponse(df)

@csrf_exempt
def participantes_filtrar(request):

    consulta_dict = json.loads(request.body.decode('utf8').replace("'", '"')) # request en formato DICCIONARIO, esto servira para trabajar los atributos en DJango

    nombre = consulta_dict["nombre"]
    cedula = consulta_dict["cedula"]
    genero = consulta_dict["genero"]
    colegio = consulta_dict["colegio"]
    carrera = consulta_dict["carrera"]
    sede = consulta_dict["sede"]
    semestre = consulta_dict["semestre"]
    estado = consulta_dict["estado"]
    municipio = consulta_dict["municipio"]

    filtro = {}
    filtroLugar = {}
    query_participante_estado = []

    lista_municipios_de_estado = []

    if nombre:
        filtro["nombre__contains"] = nombre
    
    if cedula:
        filtro["cedula"] = cedula

    if genero:
        filtro["genero"] = genero

    if colegio:
        filtro["colegio"] = colegio

    if carrera:
        filtro["carreras"] = carrera

    if sede:
        filtro["participantecarrera__sede"] = sede

    if semestre:
        filtro["participantecarrera__semestre"] = semestre

    if municipio:
        filtro["lugar"] = municipio
    elif estado:
        filtro["lugar"] = estado
        filtroLugar["fk_lugar"] = estado
        query_lugar = modelLugar.Lugar.objects.filter(**filtroLugar).values()
        dict_municipios = query_lugar.filter(fk_lugar=estado).values('id').distinct()
        
        for l in list(dict_municipios):
            lista_municipios_de_estado.append(int(l['id']))
        query_participante_estado = modelParticipante.Participante.objects.filter(lugar__in = lista_municipios_de_estado).values()
    
    query_participante = modelParticipante.Participante.objects.filter(**filtro).values()
    
    query_respuesta = json.dumps(list(query_participante) + list(query_participante_estado), cls=DjangoJSONEncoder) # Convierte el query retornado en un JSON para enviar a Vue
    return HttpResponse(query_respuesta)