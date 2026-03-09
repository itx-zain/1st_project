from rest_framework.routers import DefaultRouter
from .views import RoleViewSet, PermissionViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'userprofiles', UserProfileViewSet)

urlpatterns = router.urls