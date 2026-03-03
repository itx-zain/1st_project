from rest_framework.routers import DefaultRouter
from .views import (
    WorkspaceViewSet,
    WorkspaceMemberViewSet,
)

router = DefaultRouter()
router.register(r'workspaces', WorkspaceViewSet)
router.register(r'members', WorkspaceMemberViewSet)

urlpatterns = router.urls