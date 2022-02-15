from django.http import HttpResponse
import pandas as pd
from backend.models import modelPreguntaEdicion,modelPregunta
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers.json import DjangoJSONEncoder

@csrf_exempt
def previewPreguntas(request):
    path = request.FILES['file']
    df = pd.read_csv(path, header=0, encoding='ISO-8859-1', delimiter=',')
    return HttpResponse(df.to_json(orient="table"))

@csrf_exempt
def insertarPreguntas(request):
    data = request.body.decode('utf8').replace("'", '"')
    df = pd.DataFrame(json.loads(data))

    row_iter = df.iterrows()
    
    for index, row in row_iter:

        preguntaFilter = modelPregunta.Pregunta.objects.get(preguntaedicion__edicion=1, codigo=row[0]).values_list('id')
        if (preguntaFilter):
            pregunta = modelPregunta.Pregunta.objects.get(pk=preguntaFilter)
            pregunta.etiqueta = row[1]
            pregunta.save()
        
        else:
            modelPregunta.Pregunta.objects.create(
                codigo = row[0],
                etiqueta = row[1],
                tipo= row[2],
            )

    return HttpResponse()


    


    