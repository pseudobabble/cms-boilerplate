from rest_framework import routers

from exhibition.views import ExhibitionViewSet

router = routers.SimpleRouter()
router.register(r'exhibition-api', ExhibitionViewSet, basename='exhibition-api')
urlpatterns = router.urls

