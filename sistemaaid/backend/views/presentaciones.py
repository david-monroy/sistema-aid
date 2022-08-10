from lib2to3.pgen2.pgen import DFAState
from pptx import Presentation
from django.http import HttpResponse
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from backend.models import Pregunta,Respuesta, Estudio, Edicion
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import F
import os
from pptx.chart.data import CategoryChartData,ChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.util import Inches
from django.db.models import Count


@csrf_exempt
def crearPresentacion(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        prs = Presentation('backend/ia/presentaciones/prueba1.pptx')
        #prs = Presentation()

        slide_layout = prs.slide_layouts[0]
        slide = prs.slides.add_slide(slide_layout)

        estudioData = data['estudio']
        edicionesData = data['ediciones']
        ediciones = ''
        primero = 1

        # Guarda codigos de ediciones en un array para luego mostrarlos como subtitulo
        for edicion in edicionesData:
            if (primero == 1):
                ediciones = edicion['codigo']
                primero = 0
            else:
                ediciones = ediciones + ', ' + edicion['codigo']
        
        slide.shapes.title.text = 'Reporte de estudio ' + estudioData['nombre'] + ' - ' + estudioData['codigo']
        slide.placeholders[1].text = 'Ediciones: ' + ediciones

        i = 1
        for item in data['presentacion']: 
            print(item)
            slide_layout = prs.slide_layouts[5]
            print("entro1")
            slide = prs.slides.add_slide(slide_layout)
            print("entro2")
            preguntaData = item["pregunta"]
            print("entro3")
            pregunta = Pregunta.objects.get(pk=preguntaData["id"])
            print("entro4")
            slide.shapes.title.text = pregunta.etiqueta
            print("entro5")
            respuestas = Respuesta.objects.filter(pregunta__edicion__pk__in=item["ediciones"], pregunta__pregunta__pk=preguntaData["id"]).values(
                "respuesta").annotate(Count("id"))
            print("entro6")
            df = pd.DataFrame(respuestas)
            print("entro7")
            if (item["tipoGrafico"] == "bar"):
                print("entro")
                chart_data = CategoryChartData()
                chart_data.categories = df["respuesta"]
                chart_data.add_series('Series 1', df['id__count'])
                x, y, cx, cy = Inches(2), Inches(2), Inches(6), Inches(4.5)
                slide.shapes.add_chart(
                XL_CHART_TYPE.COLUMN_CLUSTERED, x, y, cx, cy, chart_data
                )

            if (item["tipoGrafico"] == "pie"):
                chart_data = ChartData()
                chart_data.categories = df["respuesta"]
                chart_data.add_series('Series 1', df['id__count'])
                x, y, cx, cy = Inches(2), Inches(2), Inches(6), Inches(4.5)
                slide.shapes.add_chart(
                XL_CHART_TYPE.PIE, x, y, cx, cy, chart_data
                )
            
            i+=1

        prs.save('backend/ia/presentaciones/pruebapresentaciones.pptx')

        return HttpResponse('creó la presentación')

    except BaseException as err:
        return HttpResponse(err)