import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_report_format(
    api_client,
    report,
    report_format,
):
    """Формат Report."""
    url = reverse('bizone-bug-bounty:report-detail', [report.pk])

    response = api_client.get(url)

    assert response.status_code = status.HTTP_200_OK
    assert json_response == report_format(report)


@pytest.mark.django_db()
def test_report_post(
    api_client,
):
    """Создание Report."""
    url = reverse('bizone-bug-bounty:report-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_report_delete(api_client, report):
    """Удаление Report."""
    url = reverse('bizone-bug-bounty:report-detail', [report.pk])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_report_change(
    api_client,
    report,
):
    """Изменение Report."""
    url = reverse('api:bizone-bug-bounty:report-detail', [report.pk])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
