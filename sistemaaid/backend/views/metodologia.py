from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from backend.models import Metodologia
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers.json import DjangoJSONEncoder

@csrf_exempt
def get_metodologia(request,idEdicion):
    try: 
        metodologia = Metodologia.objects.filter(edicionId_id=idEdicion).values()
        query_respuesta = json.dumps(list(metodologia), cls=DjangoJSONEncoder) 
        return HttpResponse(query_respuesta)
    except BaseException as err:
        print(err)
        return(err)