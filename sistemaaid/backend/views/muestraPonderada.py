from django.http import HttpResponse
import pandas as pd
from backend.models import MuestraPonderada, modelEdicion
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def cargarMuestra(request):
    path = request.FILES['file']
    df = pd.read_csv(path, header=0, encoding='ISO-8859-1', delimiter=',')
    totalColumnas = df.shape[1]
    tamanoMuestral = 1200
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

def insertarMuestra (request):
    path = request.FILES['file']
    df = pd.read_csv(path, header=0, encoding='ISO-8859-1', delimiter=',')
    cantidadFilas = df.shape[0]
    cantidadColumnas = df.shape[1]
    muestras = []
    for row in range(cantidadFilas):
        for column in range(1,cantidadColumnas):
            MuestraPonderada(
                    primeraCondicion = df.loc[row][0],
                    segundaCondicion = df.columns.values[column],
                    muestra = df.loc[row][column + 7],
                    poblacion = df.loc[row][column],
                    edicion = modelEdicion.Edicion.objects.get(pk=1)
            )
            muestras.append(MuestraPonderada)


    MuestraPonderada.objects.bulk_create(muestras)
    return HttpResponse(df.to_json())


    