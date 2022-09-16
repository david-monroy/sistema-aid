from rest_framework import routers, urlpatterns
from . import views
from django.urls import path, include
from .viewsets import *
from rest_framework_simplejwt import views as jwt_views

router = routers.SimpleRouter()
router.register('participantes', ParticipanteViewSet)
router.register('carreras', CarreraViewSet)
router.register('sedes', SedeViewSet)
router.register('colegios', ColegioViewSet)
router.register('participantecarreras', ParticipanteCarreraViewSet)
router.register('estudios', EstudioViewSet)
router.register('ediciones', EdicionViewSet)
router.register('muestraPonderada',MuestraPonderadaViewSet)
router.register('metodologia',MetodologiaViewSet)
router.register('preguntas',PreguntaViewSet)
router.register('listaCodigo',ListaCodigoViewSet)
router.register('categoria',CategoriaViewSet)
router.register('lugares', LugarViewSet)
router.register('preguntaEdicion', PreguntaEdicionViewSet)
router.register('grupos', GrupoViewSet)
router.register('usuarios', UsuarioViewSet)
router.register('encuestas', EncuestaViewSet)
router.register('respuestas', RespuestaViewSet)

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('participantes/participantecarreras/<int:id>', views.get_participantecarrera),
    path('muestraPonderada/cargar/<int:tamanoMuestral>', views.cargarMuestra),
    path('muestraPonderada/insertar/<int:idEdicion>', views.insertarMuestra),
    path('muestraPonderada/<int:idEdicion>', views.get_muestraPonderada),
    path('estudios/validarCodigo', views.validarCodigo),
    path('estudios/ediciones/<int:id>', views.obtenerEdiciones),
    path('estudios/seleccionarVariablesRFE/', views.seleccionarVariablesRFE),
    path('ediciones/validarCodigo', views.validarCodigoEdicion),
    path('ediciones/cargar_encuesta/<int:idEdicion>/<str:username>/', views.insertarEncuestas),
    path('ediciones/clasificar/<int:idEdicion>/', views.clasificar),
    path('ediciones/encuestas/<int:idEdicion>', views.get_encuestas),
    path('ediciones/crear-presentacion/', views.crearPresentacion),
    path('categoria/cargar/<int:idLista>', views.cargarListaCodigo),
    path('categoria/consultar/<int:idLista>', views.obtenerCategorias),
    path('participantes/agregar_masivo/', views.agregar_masivo),
    path('participantes/carga_masiva/', views.carga_masiva),
    path('participantes/participantecarreras/', views.get_participantecarrera),
    path('participantes/filtrar/', views.participantes_filtrar),
    path('participantes/obtenerEncuestas/<int:id>/', views.obtenerEncuestasParticipante),
    path('participantes/obtenerEncuestas/fechas/<int:id>/', views.obtenerEncuestasParticipantePorFechas),
    path('lugares/estados/', views.get_estados),
    path('lugares/municipios/', views.get_municipios),
    path('preguntas/cargar/<int:idEdicion>/', views.insertarPreguntas),
    path('preguntas/preview/', views.previewPreguntas),
    path('preguntas/<int:idEdicion>/', views.get_preguntas),
    path('preguntas/', views.get_preguntasPorEdiciones),
    path('usuarios/agregar/', views.agregar_usuario),
    path('usuarios/usuario', views.obtener_usuario),
    path('usuarios/', views.obtener_usuarios),
    path('usuarios/editar/<int:id>/', views.editar_usuario),
    path('metodologia/buscar/<int:idEdicion>/',views.get_metodologia),
    path('ia/entrenarModelo/', views.entrenarModelo),
    path('ia/predecir/', views.predecir),
]

urlpatterns += router.urls
