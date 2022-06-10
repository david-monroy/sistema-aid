from rest_framework import serializers
from .models import *
from django.contrib.auth.models import Group, Permission,User

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

    estudio = EstudioSerializer(read_only=True)
    estudio_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Estudio.objects.all(), source='estudio')
    class Meta:
        model = Edicion
        fields = '__all__'

class MuestraPonderadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuestraPonderada
        fields = '__all__'
        
class MetodologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metodologia
        fields = '__all__'

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = '__all__'

class PreguntaEdicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreguntaEdicion
        fields = '__all__'
class ListaCodigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaCodigo
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):

    permissions_code = serializers.StringRelatedField(many=True, source='permissions')

    class Meta:
        model = Group
        fields = [
            'id',
            'name',
            'permissions_code'
        ]

class UserSerializer(serializers.ModelSerializer):
    
    ##grupos = serializers.StringRelatedField(many=True, source='groups')
    groups = GroupSerializer(Group.objects.all(), many=True)

    class Meta:
        model = User        
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'groups'
        ]

class PermissionsSerializers(serializers.ModelSerializer):
    """
    PermissionsSerializers
    """
    class Meta:
        model = Permission
        fields = [
            'codename'
        ]
        
