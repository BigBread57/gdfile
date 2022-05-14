from rest_framework.viewsets import ModelViewSet

from server.apps.bizone_bug_bounty.api.serializers import CompanySerializer
from server.apps.bizone_bug_bounty.models import Company


class CompanyViewSet(ModelViewSet):
    """
    Компания от лица которой публикуются заявки на bug bounty.

    В описании помещается список ресурсов, где можно искать уязвимости.
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    ordering_fields = ['name', 'description', 'private']
    search_fields = ['name', 'description', 'private']
