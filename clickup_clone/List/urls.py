from rest_framework.routers import DefaultRouter
from .views import ListViewSet

router = DefaultRouter()
router.register(r'lists', ListViewSet)

urlpatterns = router.urls