# Генератор файлов для django приложения #

Gdfile - генератор начальных файлов приложения, который за основу берет модели 
из приложения. К начальным файлам относятся: представления, сериализаторы,
тесты, админ-панель, init файлы, роутер.

# Как установить # 

Pip:

```bash
pip install gdfile
  ```

Poetry:

```bash
poetry add gdfile
 ```

# Использование #

Для генерации файлов в консоли django проекта необходимо прописать команду:

```bash
gdfile -pm=path_to_folder_models -pa=path_to_api -an=app_name
 ```

Для очистки сгенерированных файлов:

```bash
gdfile -clear
 ```

Команда имеет следующие **обязательные** аргументы для работы.

1. **-pm** - Путь до папки models из текущей директории.
   Пример: server/apps/name_app/models
2. **-pa** - Путь до приложения. Пример: server.apps.name_app.
   Используется для указания корректных импортов
3. **-an** - Название приложения. Пример: app_name.

Необязательные аргументы для работы:

1. **-pmc** - Названия родительских классов моделей, кроме от models.Model и
BaseModel. Пример: BaseModel, MPTTModel
и др. Доступны разделители ';' и ','.
2. **-mf** - Поля в моделях могут быть из сторонних пакетов. Для их корректного
анализа необходимо указать информацию о них.Необходимо указать тип поля в
модели, тип поля в сериализаторе и тип поля в тестах.
Пример: PhoneField, CharField(), fake.number();
Для корректной работы необходимо поля разделить ',', а в конце поставить ';'
3. **-r** - Флаг для генерации файлов с учетом прав доступа 
(библиотеки django-rules). По умолчанию False.

Чтобы не указывать в ручную параметры сущесвует возможность указать путь до
.env файла.

```bash
$ gdfile -env=settings/config
```

В .env файле также необходимо прописать три обязательные переменные:

```yaml
# Путь до папки models из текущей директории.
GDFILE_PATH_TO_MODELS=server/apps/app_name/models

# Путь до приложения.
GDFILE_PATH_TO_API=server.apps.app_name

# Название приложения.
GDFILE_APP_NAME=app_name

# Типы полей могут использоваться из сторонних библиотек.
# Первое значение - тип поля для моделей.
# Второе значение - тип поля в сериализаторе.
# Третье значение - тип поля для тестов в библиотеке faker.
GDFILE_MODEL_FIELD=TreeForeignKey, None, fake.pyint();

# Названия родительских классов моделей, кроме от models.Model и BaseModel
GDFILE_PARENT_MODEL_CLASS=MPTTModel, ExampleModel

# Флаг для генерации файлов с учетом прав доступа
GDFILE_RULES=False
```

Информация, которая будет получена из моделей:

```
{{path_to_app}} - путь до приложения
{{app_name}} - название приложения
{{AppName}} - название приложения в верблбюжем стиле
{{app-name}} - название приложения с '-'
{{MainClass}} - название модели в верблбюжем стиле
{{main_class}} - название модели с '_'
{{mainclass}} - слитное название модели маленькими буквами 
{{main-class}} - название приложения с '-'
{{docs}} - документация модели
{{list_main_fields}} - список полей модели
fields_django_model - список полей модели с типами, указаннами в моделе
fields_for_serializers - список полей модели с типами для сериализатора
fields_for_conftest - список полей модели с типами для тестов
```

Существует возможность переопределить шаблоны файлов (только тех, которые нужны) 
для генерации. Для этого в текущем каталоге необходимо создать папку sample 
со следующей структурой:

```
sample
  ├── conftest
  │    ├── conftest_factory.py
  │    ├── conftest_fixture.py
  │    └── conftest_import.py
  ├── example_admin.py
  ├── example_init_serializer.py
  ├── example_init_view.py
  ├── example_routers.py
  ├── example_rules.py
  ├── example_serializers.py
  ├── example_tests.py
  ├── example_views.py
  └── example_views_this_rules.py
```

# Примеры сгенерированных файлов


##### Сериализатор:
```python
from rest_framework import serializers

from server.apps.mobile_provision.models import Account


class AccountSerializer(serializers.ModelSerializer):
    """Аккаунт."""

    class Meta(object):
        model = Account
        fields = ['user', 'photo', 'birth_date', 'passport_series', 'passport_number']


class AccountSerializer(serializers.Serializer):
    """Аккаунт."""

        user = serializers.None(__change_me__)
        photo = serializers.ImageField()
        birth_date = serializers.DateField()
        passport_series = serializers.CharField()
        passport_number = serializers.CharField()
```

##### Представление (доступно как с правами, так и без прав доступа)
```python
from rest_framework.viewsets import ModelViewSet

from server.apps.mobile_provision.api.serializers import AccountSerializer
from server.apps.mobile_provision.models import Account


class AccountViewSet(ModelViewSet):
    """Аккаунт."""

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    ordering_fields = ['user', 'photo', 'birth_date', 'passport_series', 'passport_number']
    search_fields = ['user', 'photo', 'birth_date', 'passport_series', 'passport_number']



from rest_framework.viewsets import ModelViewSet
from rules.contrib.rest_framework import AutoPermissionViewSetMixin

from server.apps.mobile_provision.api.serializers import AccountSerializer
from server.apps.mobile_provision.models import Account

class AccountViewSet(
    NestedViewSetMixin,
    AutoPermissionViewSetMixin,
    ModelViewSet,
):
    """Аккаунт."""

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    ordering_fields = ['user', 'photo', 'birth_date', 'passport_series', 'passport_number']
    search_fields = ['user', 'photo', 'birth_date', 'passport_series', 'passport_number']
    permission_type_map = {
        **AutoPermissionViewSetMixin.permission_type_map,
        'list': 'list',
        'metadata': None,
    }
```

##### Права доступа
```python
import rules
from rules.predicates import is_authenticated


rules.add_perm('mobile_provision.view_account', is_authenticated)
rules.add_perm('mobile_provision.add_account', is_authenticated)
rules.add_perm('mobile_provision.change_account', is_authenticated)
rules.add_perm('mobile_provision.delete_account', is_authenticated)
rules.add_perm('mobile_provision.list_account', is_authenticated)
```

##### Тесты
```python
import pytest
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse

fake = Faker()


@pytest.mark.django_db()
def test_account_format(
    api_client,
    account,
    account_format,
):
    """Формат Account."""
    url = reverse(
        'api:mobile-provision:account-detail',
        [account.pk],
    )

    json_response = api_client.get(url).json()

    assert json_response == account_format(account)


@pytest.mark.django_db()
def test_account_post(
    api_client,
):
    """Создание Account."""
    url = reverse('api:mobile-provision:account-list')
    json_response = api_client.post(
        url,
        data={},
        format='json',
    )

    assert json_response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db()
def test_account_delete(
    api_client,
    account,
):
    """Удаление Account."""
    url = reverse(
        'api:mobile-provision:account-detail',
        [account.pk],
    )

    json_response = api_client.delete(url)

    assert json_response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db()
def test_account_change(
    api_client,
    account,
):
    """Изменение Account."""
    url = reverse(
        'api:mobile-provision:account-detail',
        [account.pk],
    )

    json_response = api_client.put(
        url,
        data={},
        format='json',
    )

    assert json_response.status_code == status.HTTP_200_OK
```

##### Админка
```python
from django.contrib import admin
from server.apps.mobile_provision.model import Account


@admin.register(Account)
class ConfigurableAdmin(admin.ModelAdmin[Account]):
    """Аккаунт."""

    list_filter = ['user', 'photo', 'birth_date', 'passport_series', 'passport_number']
    search_fields = ['user', 'photo', 'birth_date', 'passport_series', 'passport_number']
    list_display = ['user', 'photo', 'birth_date', 'passport_series', 'passport_number']
```

##### Файл conftest для тестов
```python
import pytest
from factory import LazyAttribute, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker
from pytest_factoryboy import register
from rest_framework.fields import DateTimeField
from rest_framework.test import APIClient

from server.apps.mobile_provision.models import Account

fake = Faker()


class AccountFactory(DjangoModelFactory):
    """Фабрика для Account."""

    class Meta(object):
        model = Account

    user = factory.SubFactory(__change_me__)
    photo = factory.LazyAttribute(lambda account: fake.file_name())
    birth_date = factory.LazyAttribute(lambda account: fake.date_between())
    passport_series = factory.LazyAttribute(lambda account: fake.paragraph())
    passport_number = factory.LazyAttribute(lambda account: fake.paragraph())


register(Account)


@pytest.fixture
def account_format():
    """Формат Account."""
    def _account_format(account: Account):
        return {
            'id': account.pk,
            'user': account.user,
            'photo': account.photo,
            'birth_date': account.birth_date,
            'passport_series': account.passport_series,
            'passport_number': account.passport_number,
        }
    return _account_format
```

##### Файл init в папке с сериализаторами. Аналогичный создается для представлений
```python
from server.apps.app_name.api.serializer.measure_recommendation import AccountSerializer

__all__ = [
    'AccountSerializer',
]
```

##### Файл router
```python
from django.utils.translation import gettext_lazy as _
from drf_nova_router.api_router import ApiRouter
from rest_framework.routers import APIRootView

from server.apps.app_name.api.views import AccountViewSet


class AppNameAPIRootView(APIRootView):
    """Корневой view для app."""

    __doc__ = _('Приложение AppName')
    name = _('app_name')


router = ApiRouter()

router.APIRootView = AppNameAPIRootView
router.register('accounts', AccountViewSet, 'accounts')
```
