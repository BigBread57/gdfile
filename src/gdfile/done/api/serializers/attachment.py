from rest_framework import serializers

from server.apps.bizone_bug_bounty.models import Attachment


class AttachmentSerializer(serializers.ModelSerializer):
    """Вложения. Могут относиться к комментариям."""

    class Meta(object):
        model = Attachment
        fields = ['attachment', 'comment']


class AttachmentSerializer(serializers.Serializer):
    """Вложения. Могут относиться к комментариям."""

        attachment = serializers.None(__change_me__)
        comment = serializers.None(__change_me__)
