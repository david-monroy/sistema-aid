from rest_framework import serializers
from .models import Participante, Carrera, Sede, ParticipanteCarrera

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'

class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = '__all__'

class ParticipanteCarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipanteCarrera
        fields = '__all__'