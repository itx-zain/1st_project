from rest_framework.routers import DefaultRouter
from .views import (
    WorkspaceViewSet,
    WorkspaceMemberViewSet,
    RoleViewSet,
    PermissionViewSet
)

router = DefaultRouter()
router.register(r'workspaces', WorkspaceViewSet)
router.register(r'members', WorkspaceMemberViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'permissions', PermissionViewSet)

urlpatterns = router.urls

