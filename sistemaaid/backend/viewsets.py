from rest_framework import viewsets
from .models import Participante, Carrera, Sede, ParticipanteCarrera, Colegio
from .serializers import SedeSerializer, CarreraSerializer, ParticipanteCarreraSerializer,ParticipanteSerializer, ColegioSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class ColegioViewSet(viewsets.ModelViewSet):
    queryset = Colegio.objects.all()
    serializer_class = ColegioSerializer

class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer

class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer

class ParticipanteCarreraViewSet(viewsets.ModelViewSet):
    queryset = ParticipanteCarrera.objects.all()
    serializer_class = ParticipanteCarreraSerializer