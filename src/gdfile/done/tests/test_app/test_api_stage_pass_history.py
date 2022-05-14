import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_stage_pass_history_format(
    api_client,
    stage_pass_history,
    stage_pass_history_format,
):
    """Формат StagePassHistory."""
    url = reverse('bizone-bug-bounty:stage-pass-history-detail', [stage_pass_history.pk])

    response = api_client.get(url)

    assert response.status_code = status.HTTP_200_OK
    assert json_response == stage_pass_history_format(stage_pass_history)


@pytest.mark.django_db()
def test_stage_pass_history_post(
    api_client,
):
    """Создание StagePassHistory."""
    url = reverse('bizone-bug-bounty:stage-pass-history-list')
    response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_stage_pass_history_delete(api_client, stage_pass_history):
    """Удаление StagePassHistory."""
    url = reverse('bizone-bug-bounty:stage-pass-history-detail', [stage_pass_history.pk])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_stage_pass_history_change(
    api_client,
    stage_pass_history,
):
    """Изменение StagePassHistory."""
    url = reverse('api:bizone-bug-bounty:stage-pass-history-detail', [stage_pass_history.pk])

    response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert response.status_code == status.HTTP_200_OK
