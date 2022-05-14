from rest_framework.viewsets import ModelViewSet

from server.apps.bizone_bug_bounty.api.serializers import BizoneFileSerializer
from server.apps.bizone_bug_bounty.models import BizoneFile


class BizoneFileViewSet(ModelViewSet):
    """Файлы."""

    queryset = BizoneFile.objects.all()
    serializer_class = BizoneFileSerializer
    ordering_fields = []
    search_fields = []
