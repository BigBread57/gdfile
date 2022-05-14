from rest_framework import serializers

from server.apps.bizone_bug_bounty.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """Комментарий к уязвимости."""

    class Meta(object):
        model = Comment
        fields = ['user', 'report', 'text', 'creation_date', 'ip_address']


class CommentSerializer(serializers.Serializer):
    """Комментарий к уязвимости."""

        user = serializers.None(__change_me__)
        report = serializers.None(__change_me__)
        text = serializers.CharField()
        creation_date = serializers.DateTimeField()
        ip_address = serializers.IPAddressField()
