from rest_framework import serializers

from server.apps.bizone_bug_bounty.models import Company


class CompanySerializer(serializers.ModelSerializer):
    """
    Компания от лица которой публикуются заявки на bug bounty.

    В описании помещается список ресурсов, где можно искать уязвимости.
    """

    class Meta(object):
        model = Company
        fields = ['name', 'description', 'private']


class CompanySerializer(serializers.Serializer):
    """
    Компания от лица которой публикуются заявки на bug bounty.

    В описании помещается список ресурсов, где можно искать уязвимости.
    """

        name = serializers.CharField()
        description = serializers.CharField()
        private = serializers.BooleanField()
