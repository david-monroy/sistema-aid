from django.http import HttpResponse
import pandas as pd
from backend.models import modelCategoria, modelListaCodigo,Categoria
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
@csrf_exempt
def cargarListaCodigo(request,idLista):
    path = request.FILES['file']
    df = pd.read_csv(path, header=0, encoding='ISO-8859-1', delimiter=',')

    row_iter = df.iterrows()
    
    for index, row in row_iter:

        Categoria = modelCategoria.Categoria.objects.filter(codigo=row[0], listaCodigo = idLista)
        if (Categoria):
            Categoria = modelCategoria.Categoria.objects.get(codigo=row[0], listaCodigo = idLista)
            Categoria.descripcion = row[1]
            Categoria.save()
        
        else:
            modelCategoria.Categoria.objects.create(
                descripcion = row[1],
                codigo = row[0],
                listaCodigo = modelListaCodigo.ListaCodigo.objects.get(pk=idLista)
            )

    return HttpResponse()


@csrf_exempt
def obtenerCategorias(request,idLista):
    Categorias = modelCategoria.Categoria.objects.filter(listaCodigo = idLista).values()
    query_respuesta = json.dumps(list(Categorias), cls=DjangoJSONEncoder)
    return HttpResponse(query_respuesta)

    