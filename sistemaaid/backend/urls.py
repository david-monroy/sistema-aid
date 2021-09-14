from rest_framework import routers, urlpatterns
from .viewsets import ParticipanteSerializer, ParticipanteViewSet, CarreraViewSet, SedeViewSet

router = routers.SimpleRouter()
router.register('participantes', ParticipanteViewSet)
router.register('carreras', CarreraViewSet)
router.register('sedes', SedeViewSet)

urlpatterns = router.urls