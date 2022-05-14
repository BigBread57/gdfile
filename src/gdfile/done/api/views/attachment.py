from rest_framework.viewsets import ModelViewSet

from server.apps.bizone_bug_bounty.api.serializers import AttachmentSerializer
from server.apps.bizone_bug_bounty.models import Attachment


class AttachmentViewSet(ModelViewSet):
    """Вложения. Могут относиться к комментариям."""

    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    ordering_fields = ['attachment', 'comment']
    search_fields = ['attachment', 'comment']
