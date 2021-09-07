from rest_framework import routers, urlpatterns
from .viewsets import ParticipanteSerializer, ParticipanteViewSet
from . import views
from django.urls import path

router = routers.SimpleRouter()
router.register('participantes', ParticipanteViewSet)

# urlpatterns = router.urls

urlpatterns = [
    path('participantes/leer', views.leer_csv),
]

urlpatterns += router.urls