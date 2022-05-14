import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_attachment_format(
    api_client,
    attachment,
    attachment_format,
):
    """Формат Attachment."""
    url = reverse('bizone-bug-bounty:attachment-detail', [attachment.pk])

    response = api_client.get(url)

    assert response.status_code = status.HTTP_200_OK
    assert json_response == attachment_format(attachment)


@pytest.mark.django_db()
def test_attachment_post(
    api_client,
):
    """Создание Attachment."""
    url = reverse('bizone-bug-bounty:attachment-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_attachment_delete(api_client, attachment):
    """Удаление Attachment."""
    url = reverse('bizone-bug-bounty:attachment-detail', [attachment.pk])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_attachment_change(
    api_client,
    attachment,
):
    """Изменение Attachment."""
    url = reverse('api:bizone-bug-bounty:attachment-detail', [attachment.pk])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
