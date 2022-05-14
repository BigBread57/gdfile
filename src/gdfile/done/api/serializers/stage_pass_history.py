from rest_framework import serializers

from server.apps.bizone_bug_bounty.models import StagePassHistory


class StagePassHistorySerializer(serializers.ModelSerializer):
    """
    История переходов отчетов по этапам.

    Здесь должны регистрироваться все переходы отчетов.
    Будет использоваться для истории.
    Так же для понимания когда таска перешла на этап.
    """

    class Meta(object):
        model = StagePassHistory
        fields = ['stage_from', 'stage_to', 'report', 'date']


class StagePassHistorySerializer(serializers.Serializer):
    """
    История переходов отчетов по этапам.

    Здесь должны регистрироваться все переходы отчетов.
    Будет использоваться для истории.
    Так же для понимания когда таска перешла на этап.
    """

        stage_from = serializers.None(__change_me__)
        stage_to = serializers.None(__change_me__)
        report = serializers.None(__change_me__)
        date = serializers.DateTimeField()
