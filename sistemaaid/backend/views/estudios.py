from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from pandas import ExcelWriter
from backend.models import * 
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers.json import DjangoJSONEncoder

@csrf_exempt
def validarCodigo(request):
   requestToDict= json.loads(request.body.decode("utf-8").replace("'", '"'))
   estudio = modelEstudio.Estudio.objects.filter(codigo=requestToDict["codigo"])
   return HttpResponse(estudio)

@csrf_exempt
def obtenerEdiciones(request,id):
    ediciones = modelEdicion.Edicion.objects.filter(estudio_id = id).values()
    query_respuesta = json.dumps(list(ediciones), cls=DjangoJSONEncoder)
    return HttpResponse(query_respuesta)

@csrf_exempt
def seleccionarVariablesRFE(request):

   path = request.FILES['file']

   dataset = pd.read_csv(path, header=0, encoding='ISO-8859-1', delimiter=';')

   probabilidad = dataset['Probabilidad']
   entrenar = dataset.drop(['Probabilidad'], axis=1)
   rfe = RFE(RandomForestClassifier(),step = 50).fit(entrenar, probabilidad)
   selectedVariables = pd.DataFrame ({'Variables': entrenar.columns[(rfe.get_support())],
                                    'Ponderacion': rfe.estimator_.feature_importances_ })
                                    
   writer = ExcelWriter('variablesSeleccionadasPorRFE3.xlsx')
   selectedVariables.to_excel(writer, 'Hoja de datos', index=False)
   writer.save()

   print(type(selectedVariables))

   return HttpResponse(selectedVariables)