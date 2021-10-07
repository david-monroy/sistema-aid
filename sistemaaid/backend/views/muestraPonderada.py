from django.http import HttpResponse
import pandas as pd
from backend.models import MuestraPonderada
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def cargarMuestra(request):
    path = request.FILES['file']
    df = pd.read_csv(path, header=0, encoding='ISO-8859-1', delimiter=',')
    tamanoMuestral = 1200
    poblacion = df.iloc[:, 1].sum()+df.iloc[:, 2].sum()
    df['Total'] = df.iloc[:, 1]+df.iloc[:, 2]
    df['Porcentaje'] = round((df['Total']/poblacion * 100),2)
    df['Porcentaje ' + df.columns.values[1]] = (df.iloc[:, 1]/df['Total']*100).round()
    df['Porcentaje ' + df.columns.values[2]] = (df.iloc[:, 2]/df['Total']*100).round()
    df['Muestra Ponderada'] = (tamanoMuestral*df['Porcentaje']/100).round()
    row_iter = df.iterrows()

    return HttpResponse(df.head())


    