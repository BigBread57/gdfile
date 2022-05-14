from rest_framework.viewsets import ModelViewSet

from server.apps.bizone_bug_bounty.api.serializers import CommentSerializer
from server.apps.bizone_bug_bounty.models import Comment


class CommentViewSet(ModelViewSet):
    """Комментарий к уязвимости."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    ordering_fields = ['user', 'report', 'text', 'creation_date', 'ip_address']
    search_fields = ['user', 'report', 'text', 'creation_date', 'ip_address']
