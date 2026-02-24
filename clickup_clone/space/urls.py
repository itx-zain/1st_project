from rest_framework.routers import DefaultRouter
from .views import SpaceViewSet  

router = DefaultRouter()
router.register(r'spaces', SpaceViewSet)

urlpatterns = router.urls