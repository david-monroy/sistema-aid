from lib2to3.pgen2.pgen import DFAState
from pptx import Presentation
from django.http import HttpResponse
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from backend.models import Pregunta,Respuesta
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import F
import os
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.util import Inches
from django.db.models import Count


@csrf_exempt
def crearPresentacion(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        prs = Presentation('backend/ia/presentaciones/prueba1.pptx')
        slide_layout = prs.slide_layouts[1]
        slide = prs.slides.add_slide(slide_layout)
        preguntaData = data["pregunta"]
        pregunta = Pregunta.objects.get(pk=preguntaData["id"])
        slide.shapes.title.text = pregunta.etiqueta
        respuestas = Respuesta.objects.filter(pregunta__edicion__pk__in=data["ediciones"], pregunta__pregunta__pk=preguntaData["id"]).values(
            "respuesta").annotate(Count("id"))
        df = pd.DataFrame(respuestas)
        
        if (data["tipoGrafico"] == "bar"):
            chart_data = CategoryChartData()
            chart_data.categories = df["respuesta"]
            chart_data.add_series('Series 1', df['id__count'])
            x, y, cx, cy = Inches(2), Inches(2), Inches(6), Inches(4.5)
            slide.shapes.add_chart(
            XL_CHART_TYPE.COLUMN_CLUSTERED, x, y, cx, cy, chart_data
            )
        prs.save('backend/ia/presentaciones/pruebapresentaciones.pptx')

        return HttpResponse('creó la presentación')

    except BaseException as err:
        return HttpResponse(err)