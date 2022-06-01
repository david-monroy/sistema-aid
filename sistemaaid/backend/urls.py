from rest_framework import routers, urlpatterns
from . import views
from django.urls import path
from .viewsets import EstudioViewSet, ParticipanteViewSet, CarreraViewSet, SedeViewSet, ParticipanteCarreraViewSet, ColegioViewSet
from rest_framework_simplejwt import views as jwt_views

router = routers.SimpleRouter()
router.register('participantes', ParticipanteViewSet)
router.register('carreras', CarreraViewSet)
router.register('sedes', SedeViewSet)
router.register('colegios', ColegioViewSet)
router.register('participantecarreras', ParticipanteCarreraViewSet)
router.register('estudios', EstudioViewSet)

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('participantes/agregar_masivo/', views.agregar_masivo),
    path('participantes/editar_masivo/', views.editar_masivo),
    path('participantes/participantecarreras/', views.get_participantecarrera),
    path('participantes/filtrar/', views.participantes_filtrar),
]

urlpatterns += router.urls


