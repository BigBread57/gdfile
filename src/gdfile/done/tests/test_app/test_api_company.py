import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_company_format(
    api_client,
    company,
    company_format,
):
    """Формат Company."""
    url = reverse('bizone-bug-bounty:company-detail', [company.pk])

    response = api_client.get(url)

    assert response.status_code = status.HTTP_200_OK
    assert json_response == company_format(company)


@pytest.mark.django_db()
def test_company_post(
    api_client,
):
    """Создание Company."""
    url = reverse('bizone-bug-bounty:company-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_company_delete(api_client, company):
    """Удаление Company."""
    url = reverse('bizone-bug-bounty:company-detail', [company.pk])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_company_change(
    api_client,
    company,
):
    """Изменение Company."""
    url = reverse('api:bizone-bug-bounty:company-detail', [company.pk])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
