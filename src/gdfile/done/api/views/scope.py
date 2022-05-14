from rest_framework.viewsets import ModelViewSet

from server.apps.bizone_bug_bounty.api.serializers import ScopeSerializer
from server.apps.bizone_bug_bounty.models import Scope


class ScopeViewSet(ModelViewSet):
    """
    Скоуп компании.

    Список наград компании, к ним привязывается отчет.
    Проставляется только критичность и оплачивается или нет.
    """

    queryset = Scope.objects.all()
    serializer_class = ScopeSerializer
    ordering_fields = ['company', 'critical_type', 'asset', 'eligibility', 'in_scope']
    search_fields = ['company', 'critical_type', 'asset', 'eligibility', 'in_scope']
