from rest_framework.viewsets import ModelViewSet

from server.apps.bizone_bug_bounty.api.serializers import ReportSerializer
from server.apps.bizone_bug_bounty.models import Report


class ReportViewSet(ModelViewSet):
    """Отчет о найденной уязвимости."""

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    ordering_fields = ['user', 'name', 'critical_type', 'cvss', 'scope', 'description', 'impact', 'creation_date', 'modification_date', 'visibility', 'current_stage']
    search_fields = ['user', 'name', 'critical_type', 'cvss', 'scope', 'description', 'impact', 'creation_date', 'modification_date', 'visibility', 'current_stage']
