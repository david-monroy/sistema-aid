from django.http import HttpResponse
import pandas as pd
from backend.models import MuestraPonderada, modelEdicion
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
@csrf_exempt
def cargarMuestra(request, tamanoMuestral):
    path = request.FILES['file']
    df = pd.read_excel(path)
    totalColumnas = df.shape[1]
    poblacion = df.iloc[:, 1:df.shape[1]].sum()
    totalPoblacion = 0
    for i in poblacion.values.tolist():
       totalPoblacion += i

    df['Total'] = df.sum(axis=1)
    df['Porcentaje']=round((df['Total']/totalPoblacion * 100),2)
    df['Muestra Ponderada'] = (tamanoMuestral*df['Porcentaje']/100).round()

    for column in range(1,totalColumnas):
        df['Porcentaje ' + df.columns.values[column]] = (df.iloc[:, column]/df['Total']*100).round()
        df['Muestra ' + df.columns.values[column]] = (df['Muestra Ponderada']*df['Porcentaje ' + df.columns.values[column]]/100).round()

    return HttpResponse(df.to_json(orient="table"))

@csrf_exempt
def insertarMuestra (request, idEdicion):
    data = request.body.decode('utf8').replace("'", '"')
    df = pd.DataFrame(json.loads(data))
    cantidadFilas = df.shape[0]
    cantidadColumnas = df.shape[1]
    muestras = []
    for column in range (1,df.shape[1]):
        if df.columns.values[column] == "Total":
            cantidadColumnas = column 
            break

    for row in range(cantidadFilas):
        for column in range(2,cantidadColumnas):
            muestras.append(MuestraPonderada(
                primeraCondicion=df.loc[row][1],
                segundaCondicion=df.columns.values[column],
                poblacion=df.loc[row][column], 
                muestra = df.loc[row]['Muestra ' + df.columns.values[column]],
                edicion = modelEdicion.Edicion.objects.get(pk=idEdicion)
            ))

    msj =  MuestraPonderada.objects.bulk_create(muestras)
    return HttpResponse()

@csrf_exempt
def get_muestraPonderada(request,idEdicion):
    try: 
        muestraPonderada = MuestraPonderada.objects.filter(edicion_id=idEdicion).values()
        query_respuesta = json.dumps(list(muestraPonderada), cls=DjangoJSONEncoder) 
        return HttpResponse(query_respuesta)
    except BaseException as err:
        print(err)
        return(err)


    