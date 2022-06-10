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

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('participantes/participantecarreras/<int:id>', views.get_participantecarrera),
    path('muestraPonderada/cargar/<int:tamanoMuestral>', views.cargarMuestra),
    path('muestraPonderada/insertar/<int:idEdicion>', views.insertarMuestra),
    path('estudios/validarCodigo', views.validarCodigo),
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
    path('usuarios/usuario', views.obtener_usuario),
    path('usuarios/', views.obtener_usuarios),
   ### path('usuario/<int:id>/', views.obtener_usuario_id),
    path('estudios/ediciones/<int:id>', views.obtenerEdiciones),
    path('estudios/seleccionarVariablesRFE/', views.seleccionarVariablesRFE),
]

urlpatterns += router.urls
