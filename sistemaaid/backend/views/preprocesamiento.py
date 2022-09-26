import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F,CharField, Value as V
from backend.response import *
from django.http import HttpResponse
from tkinter.filedialog import asksaveasfilename

@csrf_exempt
def preprocesamiento(request):
    try:
        path = request.FILES['file']
        df = pd.read_excel(path)
        df = df.dropna(axis=1, how='all', inplace=False)
        df =df.replace(-777777777,)
        df =df.replace(-999999999,)
        file_name = asksaveasfilename(filetypes=[('excel file', '*.xlsx')], defaultextension='.xlsx')
        df.to_excel(file_name)
        return HttpResponse(response(message="Se preproceso todo correctamente"))

    except BaseException as err:
        return HttpResponse(error_response(message="Ha ocurrido un error", error=err.args))

@csrf_exempt
def preprocesamientoArboles(request):
    try:
        path = request.FILES['file']
        datos = pd.read_excel(path)
        #onehotcodifier
        for i in range(0,datos.shape[1]):
            clasificacion = pd.get_dummies(datos.iloc[:,i], prefix=datos.columns[i])
            datos= datos.join(clasificacion)

        datos = datos.drop(datos.iloc[:, 0:i],axis = 1)

        datos.to_excel('Historicos Monitor/completo arbol limpio.xlsx')
        return HttpResponse(response(message="Se insertaron correctamente las " + df.shape[1] + " encuestas"))

    except BaseException as err:
        return HttpResponse(error_response(message="Ha ocurrido un error", error=err.args))