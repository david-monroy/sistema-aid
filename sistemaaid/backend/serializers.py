from rest_framework import serializers
from .models import *

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'

class ColegioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colegio
        fields = '__all__'

class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = '__all__'

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'

class ParticipanteSerializer(serializers.ModelSerializer):
    colegio = ColegioSerializer(read_only=True, required=False, allow_null=True)
    colegio_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Colegio.objects.all(), source='colegio',required=False, allow_null=True)
    lugar = LugarSerializer(read_only=True, required=False, allow_null=True)
    lugar_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Lugar.objects.all(), source='lugar',required=False, allow_null=True)
    class Meta:
        model = Participante
        fields = '__all__'

class ParticipanteCarreraSerializer(serializers.ModelSerializer):
    carrera = CarreraSerializer(read_only=True)
    carrera_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Carrera.objects.all(), source='carrera')
    sede = SedeSerializer(read_only=True)
    sede_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Sede.objects.all(), source='sede')
    participante = ParticipanteSerializer(read_only=True)
    participante_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Participante.objects.all(), source='participante')
    class Meta:
        model = ParticipanteCarrera
        fields = '__all__'


class EstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudio
        fields = '__all__'


class EdicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edicion
        fields = '__all__'

class MuestraPonderadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuestraPonderada
        fields = '__all__'
        