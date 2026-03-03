from rest_framework.routers import DefaultRouter

from workspace.urls import urlpatterns
from .views import RoleViewSet,PermissionViewSet

router = DefaultRouter()
router.register(r'role',RoleViewSet)
router.register(r'permission',PermissionViewSet)
urlpatterns = router.urls