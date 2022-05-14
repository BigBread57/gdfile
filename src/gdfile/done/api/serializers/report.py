from rest_framework import serializers

from server.apps.bizone_bug_bounty.models import Report


class ReportSerializer(serializers.ModelSerializer):
    """Отчет о найденной уязвимости."""

    class Meta(object):
        model = Report
        fields = ['user', 'name', 'critical_type', 'cvss', 'scope', 'description', 'impact', 'creation_date', 'modification_date', 'visibility', 'current_stage']


class ReportSerializer(serializers.Serializer):
    """Отчет о найденной уязвимости."""

        user = serializers.None(__change_me__)
        name = serializers.CharField()
        critical_type = serializers.CharField()
        cvss = serializers.DecimalField()
        scope = serializers.None(__change_me__)
        description = serializers.CharField()
        impact = serializers.CharField()
        creation_date = serializers.DateTimeField()
        modification_date = serializers.DateTimeField()
        visibility = serializers.CharField()
        current_stage = serializers.None(__change_me__)
