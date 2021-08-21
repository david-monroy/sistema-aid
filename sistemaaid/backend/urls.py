from rest_framework import routers, urlpatterns
from .viewsets import ParticipanteSerializer, ParticipanteViewSet

router = routers.SimpleRouter()
router.register('participantes', ParticipanteViewSet)

urlpatterns = router.urls