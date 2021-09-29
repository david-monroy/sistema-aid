from rest_framework import routers, urlpatterns
from . import views
from django.urls import path
from .viewsets import ParticipanteSerializer, ParticipanteViewSet, CarreraViewSet, SedeViewSet, ParticipanteCarreraViewSet, ColegioViewSet

router = routers.SimpleRouter()
router.register('participantes', ParticipanteViewSet)
router.register('carreras', CarreraViewSet)
router.register('sedes', SedeViewSet)
router.register('colegios', ColegioViewSet)
router.register('participantecarreras', ParticipanteCarreraViewSet)

# urlpatterns = router.urls

urlpatterns = [
    path('participantes/leer', views.leer_csv),
    path('participantes/leer/actualizar', views.leer_csv_actualizar),
    path('participantes/participantecarreras', views.get_participantecarrera),
    path('participantes/filtrar', views.participantes_filtrar),
]

urlpatterns += router.urls