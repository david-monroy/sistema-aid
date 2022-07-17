from django.http import HttpResponse
import pandas as pd
from backend.models import Pregunta, PreguntaEdicion, Edicion
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers.json import DjangoJSONEncoder

from backend.models.modelListaCodigo import ListaCodigo

@csrf_exempt
def previewPreguntas(request):
    path = request.FILES['file']
    df = pd.read_excel(path)
    return HttpResponse(df.to_json(orient="table"))

@csrf_exempt
def insertarPreguntas(request, idEdicion):
    data = request.body.decode('utf8').replace("'", '"')
    df = pd.DataFrame(json.loads(data))
    row_iter = df.iterrows()
    for index, row in row_iter:
        listaCodigo = None
        if (row[3] == 'Cadena'):
                listaCodigo = asignarListaCodigo(row[2])
        preguntaFilter = Pregunta.objects.filter(preguntaedicion__edicion=idEdicion, codigo=row[1])
        if (preguntaFilter):
            pregunta = Pregunta.objects.get(preguntaedicion__edicion=idEdicion, codigo=row[1])
            pregunta.etiqueta = row[2]
            pregunta.tipo = row[3]
            if (listaCodigo != None):
                listaCodigo = asignarListaCodigo(row[2])
            pregunta.save()
        else:
            if (listaCodigo != None):
                
                nueva_pregunta = Pregunta.objects.create(
                    codigo = row[1],
                    etiqueta = row[2],
                    tipo= row[3],
                    listaCodigo = asignarListaCodigo(row[2])    
                )
            else:

                nueva_pregunta = Pregunta.objects.create(
                    codigo = row[1],
                    etiqueta = row[2],
                    tipo= row[3] 
                )

            PreguntaEdicion.objects.create(
                pregunta = nueva_pregunta,
                edicion = Edicion.objects.get(pk=idEdicion)
            )
    return HttpResponse()

def asignarListaCodigo(etiqueta):
    listaCodigo = None
    if (ListaCodigo.objects.filter(nombre=etiqueta)):
        listaCodigo = ListaCodigo.objects.get(nombre=etiqueta)
    return listaCodigo

@csrf_exempt
def get_preguntas(request,idEdicion):
    try: 
        preguntas = Pregunta.objects.filter(preguntaedicion__edicion=idEdicion).values()
        query_respuesta = json.dumps(list(preguntas), cls=DjangoJSONEncoder) 
        return HttpResponse(query_respuesta)
    except BaseException as err:
        print(err)
        return(err)





    


    