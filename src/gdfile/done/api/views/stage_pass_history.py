from rest_framework.viewsets import ModelViewSet

from server.apps.bizone_bug_bounty.api.serializers import StagePassHistorySerializer
from server.apps.bizone_bug_bounty.models import StagePassHistory


class StagePassHistoryViewSet(ModelViewSet):
    """
    История переходов отчетов по этапам.

    Здесь должны регистрироваться все переходы отчетов.
    Будет использоваться для истории.
    Так же для понимания когда таска перешла на этап.
    """

    queryset = StagePassHistory.objects.all()
    serializer_class = StagePassHistorySerializer
    ordering_fields = ['stage_from', 'stage_to', 'report', 'date']
    search_fields = ['stage_from', 'stage_to', 'report', 'date']
