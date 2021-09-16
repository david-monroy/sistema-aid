from rest_framework import viewsets
from .models import Participante
from .serializers import ParticipanteSerializer
from .models import Carrera
from .serializers import CarreraSerializer
from .models import Sede
from .serializers import SedeSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer

class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer