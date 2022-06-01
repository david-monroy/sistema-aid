from rest_framework import routers, urlpatterns
from . import views
<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import path
<<<<<<< HEAD
>>>>>>> 90e4720eda23bb18385e64b04cefeb1a0ccab7a4
from .viewsets import *
=======
from .viewsets import EstudioViewSet, ParticipanteViewSet, CarreraViewSet, SedeViewSet, ParticipanteCarreraViewSet, ColegioViewSet, EdicionViewSet
>>>>>>> 708883dbad694a00eba065c470171258dd18f353
from rest_framework_simplejwt import views as jwt_views

router = routers.SimpleRouter()
router.register('participantes', ParticipanteViewSet)
router.register('carreras', CarreraViewSet)
router.register('sedes', SedeViewSet)
router.register('colegios', ColegioViewSet)
router.register('participantecarreras', ParticipanteCarreraViewSet)
router.register('estudios', EstudioViewSet)
router.register('ediciones', EdicionViewSet)
<<<<<<< HEAD
router.register('muestraPonderada',MuestraPonderadaViewSet)
<<<<<<< HEAD
router.register('metodologia',MetodologiaViewSet)
router.register('preguntas',PreguntaViewSet)
router.register('listaCodigo',ListaCodigoViewSet)
router.register('categoria',CategoriaViewSet)
router.register('lugares', LugarViewSet)
<<<<<<< HEAD
=======

>>>>>>> 90e4720eda23bb18385e64b04cefeb1a0ccab7a4
=======
>>>>>>> 708883dbad694a00eba065c470171258dd18f353
=======
router.register('preguntaEdicion', PreguntaEdicionViewSet)
>>>>>>> a33aee54cd3c259c1f9d06de5baaf78c541f536a

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('participantes/participantecarreras/<int:id>', views.get_participantecarrera),
    path('muestraPonderada/cargar/<int:tamanoMuestral>', views.cargarMuestra),
    path('muestraPonderada/insertar/<int:idEdicion>', views.insertarMuestra),
    path('estudios/validarCodigo', views.validarCodigo),
<<<<<<< HEAD
    path('ediciones/validarCodigo', views.validarCodigo),
    path('categoria/cargar/<int:idLista>', views.cargarListaCodigo),
    path('categoria/consultar/<int:idLista>', views.obtenerCategorias),
    path('participantes/agregar_masivo/', views.agregar_masivo),
    path('participantes/carga_masiva/', views.carga_masiva),
    path('participantes/participantecarreras/', views.get_participantecarrera),
    path('participantes/filtrar/', views.participantes_filtrar),
    path('lugares/estados/', views.get_estados),
    path('lugares/municipios/', views.get_municipios),
    path('preguntas/cargar/<int:idEdicion>/', views.insertarPreguntas),
    path('preguntas/preview/', views.previewPreguntas),
    path('usuarios/agregar/', views.agregar_usuario),
    path('usuarios/', views.obtener_usuarios),
    path('usuarios/grupos/', views.obtener_grupos),
    path('estudios/ediciones/<int:id>', views.obtenerEdiciones),
<<<<<<< HEAD
=======
    path('ediciones/validarCodigo', views.validarCodigo)
>>>>>>> 90e4720eda23bb18385e64b04cefeb1a0ccab7a4
=======
    path('estudios/seleccionarVariablesRFE/', views.seleccionarVariablesRFE),
>>>>>>> 4c47022cd3a0b138943943605d473169b43d99e6
]

urlpatterns += router.urls
