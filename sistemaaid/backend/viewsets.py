from rest_framework import viewsets
from .models import *
from .serializers import *

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class ColegioViewSet(viewsets.ModelViewSet):
    queryset = Colegio.objects.all()
    serializer_class = ColegioSerializer

class LugarViewSet(viewsets.ModelViewSet):
    queryset = Lugar.objects.all()
    serializer_class = LugarSerializer

class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer

class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer

class ParticipanteCarreraViewSet(viewsets.ModelViewSet):
    queryset = ParticipanteCarrera.objects.all()
    serializer_class = ParticipanteCarreraSerializer

#ESTUDIOS 

class EstudioViewSet(viewsets.ModelViewSet):
    queryset = Estudio.objects.all()
    serializer_class = EstudioSerializer


class EdicionViewSet(viewsets.ModelViewSet):
    queryset = Edicion.objects.all()
<<<<<<< HEAD
    serializer_class = EdicionSerializer

class MuestraPonderadaViewSet(viewsets.ModelViewSet):
    queryset = MuestraPonderada.objects.all()
<<<<<<< HEAD
    serializer_class = MuestraPonderadaSerializer

class MetodologiaViewSet(viewsets.ModelViewSet):
    queryset = Metodologia.objects.all()
    serializer_class = MetodologiaSerializer

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer

class PreguntaEdicionViewSet(viewsets.ModelViewSet):
    queryset = PreguntaEdicion.objects.all()
    serializer_class = PreguntaEdicionSerializer
class ListaCodigoViewSet(viewsets.ModelViewSet):
    queryset = ListaCodigo.objects.all()
    serializer_class = ListaCodigoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
=======
    serializer_class = MuestraPonderadaSerializer
>>>>>>> 90e4720eda23bb18385e64b04cefeb1a0ccab7a4
=======
    serializer_class = EdicionSerializer
>>>>>>> 708883dbad694a00eba065c470171258dd18f353
