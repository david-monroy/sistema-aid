from rest_framework import routers, urlpatterns
from . import views
from django.urls import path
from .viewsets import ParticipanteSerializer, ParticipanteViewSet, CarreraViewSet, SedeViewSet, ParticipanteCarreraViewSet

router = routers.SimpleRouter()
router.register('participantes', ParticipanteViewSet)
router.register('carreras', CarreraViewSet)
router.register('sedes', SedeViewSet)
router.register('participantecarreras', SedeViewSet)

# urlpatterns = router.urls

urlpatterns = [
    path('participantes/leer', views.leer_csv),
]

urlpatterns += router.urls