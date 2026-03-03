from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Workspace, WorkspaceMember
from .serializers import WorkspaceSerializer, WorkspaceMemberSerializer


class WorkspaceViewSet(viewsets.ModelViewSet):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer

    def destroy(self, request, *args, **kwargs):
        workspace = self.get_object()
        workspace.soft_delete()
        return Response(
            {"message": "Workspace soft deleted successfully"},
            status=status.HTTP_200_OK
        )


class WorkspaceMemberViewSet(viewsets.ModelViewSet):
    queryset = WorkspaceMember.objects.all()
    serializer_class = WorkspaceMemberSerializer