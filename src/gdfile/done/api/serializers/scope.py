from rest_framework import serializers

from server.apps.bizone_bug_bounty.models import Scope


class ScopeSerializer(serializers.ModelSerializer):
    """
    Скоуп компании.

    Список наград компании, к ним привязывается отчет.
    Проставляется только критичность и оплачивается или нет.
    """

    class Meta(object):
        model = Scope
        fields = ['company', 'critical_type', 'asset', 'eligibility', 'in_scope']


class ScopeSerializer(serializers.Serializer):
    """
    Скоуп компании.

    Список наград компании, к ним привязывается отчет.
    Проставляется только критичность и оплачивается или нет.
    """

        company = serializers.None(__change_me__)
        critical_type = serializers.CharField()
        asset = serializers.CharField()
        eligibility = serializers.BooleanField()
        in_scope = serializers.BooleanField()
