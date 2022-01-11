from rest_framework import routers, urlpatterns
from . import views
from django.urls import path
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


urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('participantes/leer', views.leer_csv),
    path('participantes/leer/actualizar', views.leer_csv_actualizar),
    path('participantes/participantecarreras/<int:id>', views.get_participantecarrera),
    path('muestraPonderada/cargar/<int:tamanoMuestral>', views.cargarMuestra),
    path('muestraPonderada/insertar/<int:idEdicion>', views.insertarMuestra),
    path('estudios/validarCodigo', views.validarCodigo),
    path('ediciones/validarCodigo', views.validarCodigo)
]

urlpatterns += router.urls


