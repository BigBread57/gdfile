from django.contrib import admin
from server.apps.bizone_bug_bounty.model import Attachment, BizoneFile, Comment, Report, Scope, Company, StagePassHistory


@admin.register(Attachment)
class ConfigurableAdmin(admin.ModelAdmin[Attachment]):
    """Вложения. Могут относиться к комментариям."""

    list_filter = ['attachment', 'comment']
    search_fields = ['attachment', 'comment']
    list_display = ['attachment', 'comment']


@admin.register(BizoneFile)
class ConfigurableAdmin(admin.ModelAdmin[BizoneFile]):
    """Файлы."""

    list_filter = []
    search_fields = []
    list_display = []


@admin.register(Comment)
class ConfigurableAdmin(admin.ModelAdmin[Comment]):
    """Комментарий к уязвимости."""

    list_filter = ['user', 'report', 'text', 'creation_date', 'ip_address']
    search_fields = ['user', 'report', 'text', 'creation_date', 'ip_address']
    list_display = ['user', 'report', 'text', 'creation_date', 'ip_address']


@admin.register(Report)
class ConfigurableAdmin(admin.ModelAdmin[Report]):
    """Отчет о найденной уязвимости."""

    list_filter = ['user', 'name', 'critical_type', 'cvss', 'scope', 'description', 'impact', 'creation_date', 'modification_date', 'visibility', 'current_stage']
    search_fields = ['user', 'name', 'critical_type', 'cvss', 'scope', 'description', 'impact', 'creation_date', 'modification_date', 'visibility', 'current_stage']
    list_display = ['user', 'name', 'critical_type', 'cvss', 'scope', 'description', 'impact', 'creation_date', 'modification_date', 'visibility', 'current_stage']


@admin.register(Scope)
class ConfigurableAdmin(admin.ModelAdmin[Scope]):
    """
    Скоуп компании.

    Список наград компании, к ним привязывается отчет.
    Проставляется только критичность и оплачивается или нет.
    """

    list_filter = ['company', 'critical_type', 'asset', 'eligibility', 'in_scope']
    search_fields = ['company', 'critical_type', 'asset', 'eligibility', 'in_scope']
    list_display = ['company', 'critical_type', 'asset', 'eligibility', 'in_scope']


@admin.register(Company)
class ConfigurableAdmin(admin.ModelAdmin[Company]):
    """
    Компания от лица которой публикуются заявки на bug bounty.

    В описании помещается список ресурсов, где можно искать уязвимости.
    """

    list_filter = ['name', 'description', 'private']
    search_fields = ['name', 'description', 'private']
    list_display = ['name', 'description', 'private']


@admin.register(StagePassHistory)
class ConfigurableAdmin(admin.ModelAdmin[StagePassHistory]):
    """
    История переходов отчетов по этапам.

    Здесь должны регистрироваться все переходы отчетов.
    Будет использоваться для истории.
    Так же для понимания когда таска перешла на этап.
    """

    list_filter = ['stage_from', 'stage_to', 'report', 'date']
    search_fields = ['stage_from', 'stage_to', 'report', 'date']
    list_display = ['stage_from', 'stage_to', 'report', 'date']
