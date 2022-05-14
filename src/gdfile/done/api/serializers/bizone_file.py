from rest_framework import serializers

from server.apps.bizone_bug_bounty.models import BizoneFile


class BizoneFileSerializer(serializers.ModelSerializer):
    """Файлы."""

    class Meta(object):
        model = BizoneFile
        fields = []


class BizoneFileSerializer(serializers.Serializer):
    """Файлы."""

