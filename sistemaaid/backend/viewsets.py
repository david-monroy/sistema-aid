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
    serializer_class = EdicionSerializer

class MuestraPonderadaViewSet(viewsets.ModelViewSet):
    queryset = MuestraPonderada.objects.all()
    serializer_class = MuestraPonderadaSerializer

class MetodologiaViewSet(viewsets.ModelViewSet):
    queryset = Metodologia.objects.all()
    serializer_class = MetodologiaSerializer
class ListaCodigoViewSet(viewsets.ModelViewSet):
    queryset = ListaCodigo.objects.all()
    serializer_class = ListaCodigoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
