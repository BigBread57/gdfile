import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_scope_format(
    api_client,
    scope,
    scope_format,
):
    """Формат Scope."""
    url = reverse('bizone-bug-bounty:scope-detail', [scope.pk])

    response = api_client.get(url)

    assert response.status_code = status.HTTP_200_OK
    assert json_response == scope_format(scope)


@pytest.mark.django_db()
def test_scope_post(
    api_client,
):
    """Создание Scope."""
    url = reverse('bizone-bug-bounty:scope-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_scope_delete(api_client, scope):
    """Удаление Scope."""
    url = reverse('bizone-bug-bounty:scope-detail', [scope.pk])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_scope_change(
    api_client,
    scope,
):
    """Изменение Scope."""
    url = reverse('api:bizone-bug-bounty:scope-detail', [scope.pk])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
