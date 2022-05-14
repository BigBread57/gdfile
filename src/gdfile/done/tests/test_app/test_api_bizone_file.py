import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_bizone_file_format(
    api_client,
    bizone_file,
    bizone_file_format,
):
    """Формат BizoneFile."""
    url = reverse('bizone-bug-bounty:bizone-file-detail', [bizone_file.pk])

    response = api_client.get(url)

    assert response.status_code = status.HTTP_200_OK
    assert json_response == bizone_file_format(bizone_file)


@pytest.mark.django_db()
def test_bizone_file_post(
    api_client,
):
    """Создание BizoneFile."""
    url = reverse('bizone-bug-bounty:bizone-file-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_bizone_file_delete(api_client, bizone_file):
    """Удаление BizoneFile."""
    url = reverse('bizone-bug-bounty:bizone-file-detail', [bizone_file.pk])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_bizone_file_change(
    api_client,
    bizone_file,
):
    """Изменение BizoneFile."""
    url = reverse('api:bizone-bug-bounty:bizone-file-detail', [bizone_file.pk])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
