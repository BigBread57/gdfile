import pytest
from factory import LazyAttribute, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker
from pytest_factoryboy import register
from rest_framework.fields import DateTimeField
from rest_framework.test import APIClient

from server.apps.bizone_bug_bounty.models import Attachment

fake = Faker()


class AttachmentFactory(DjangoModelFactory):
    """Фабрика для Attachment."""

    class Meta(object):
        model = Attachment

    attachment = factory.SubFactory(__change_me__)
    comment = factory.SubFactory(__change_me__)


class BizoneFileFactory(DjangoModelFactory):
    """Фабрика для BizoneFile."""

    class Meta(object):
        model = BizoneFile



class CommentFactory(DjangoModelFactory):
    """Фабрика для Comment."""

    class Meta(object):
        model = Comment

    user = factory.SubFactory(__change_me__)
    report = factory.SubFactory(__change_me__)
    text = factory.LazyAttribute(lambda comment: fake.paragraph())
    creation_date = factory.LazyAttribute(lambda comment: fake.date_time_this_month())
    ip_address = factory.LazyAttribute(lambda comment: fake.ipv4())


class ReportFactory(DjangoModelFactory):
    """Фабрика для Report."""

    class Meta(object):
        model = Report

    user = factory.SubFactory(__change_me__)
    name = factory.LazyAttribute(lambda report: fake.paragraph())
    critical_type = factory.LazyAttribute(lambda report: fake.paragraph())
    cvss = factory.LazyAttribute(lambda report: fake.pydecimal())
    scope = factory.SubFactory(__change_me__)
    description = factory.LazyAttribute(lambda report: fake.paragraph())
    impact = factory.LazyAttribute(lambda report: fake.paragraph())
    creation_date = factory.LazyAttribute(lambda report: fake.date_time_this_month())
    modification_date = factory.LazyAttribute(lambda report: fake.date_time_this_month())
    visibility = factory.LazyAttribute(lambda report: fake.paragraph())
    current_stage = factory.SubFactory(__change_me__)


class ScopeFactory(DjangoModelFactory):
    """Фабрика для Scope."""

    class Meta(object):
        model = Scope

    company = factory.SubFactory(__change_me__)
    critical_type = factory.LazyAttribute(lambda scope: fake.paragraph())
    asset = factory.LazyAttribute(lambda scope: fake.paragraph())
    eligibility = factory.LazyAttribute(lambda scope: fake.pybool())
    in_scope = factory.LazyAttribute(lambda scope: fake.pybool())


class CompanyFactory(DjangoModelFactory):
    """Фабрика для Company."""

    class Meta(object):
        model = Company

    name = factory.LazyAttribute(lambda company: fake.paragraph())
    description = factory.LazyAttribute(lambda company: fake.paragraph())
    private = factory.LazyAttribute(lambda company: fake.pybool())


class StagePassHistoryFactory(DjangoModelFactory):
    """Фабрика для StagePassHistory."""

    class Meta(object):
        model = StagePassHistory

    stage_from = factory.SubFactory(__change_me__)
    stage_to = factory.SubFactory(__change_me__)
    report = factory.SubFactory(__change_me__)
    date = factory.LazyAttribute(lambda stage_pass_history: fake.date_time_this_month())


register(StagePassHistory)
register(Company)
register(Scope)
register(Report)
register(Comment)
register(BizoneFile)
register(Attachment)


@pytest.fixture
def attachment_format():
    """Формат Attachment."""
    def _attachment_format(attachment: Attachment):
        return {
            'id': attachment.pk,
            'attachment': attachment.attachment,
            'comment': attachment.comment,
        }
    return _attachment_format


@pytest.fixture
def bizone_file_format():
    """Формат BizoneFile."""
    def _bizone_file_format(bizone_file: BizoneFile):
        return {
            'id': bizone_file.pk,
        }
    return _bizone_file_format


@pytest.fixture
def comment_format():
    """Формат Comment."""
    def _comment_format(comment: Comment):
        return {
            'id': comment.pk,
            'user': comment.user,
            'report': comment.report,
            'text': comment.text,
            'creation_date': comment.creation_date,
            'ip_address': comment.ip_address,
        }
    return _comment_format


@pytest.fixture
def report_format():
    """Формат Report."""
    def _report_format(report: Report):
        return {
            'id': report.pk,
            'user': report.user,
            'name': report.name,
            'critical_type': report.critical_type,
            'cvss': report.cvss,
            'scope': report.scope,
            'description': report.description,
            'impact': report.impact,
            'creation_date': report.creation_date,
            'modification_date': report.modification_date,
            'visibility': report.visibility,
            'current_stage': report.current_stage,
        }
    return _report_format


@pytest.fixture
def scope_format():
    """Формат Scope."""
    def _scope_format(scope: Scope):
        return {
            'id': scope.pk,
            'company': scope.company,
            'critical_type': scope.critical_type,
            'asset': scope.asset,
            'eligibility': scope.eligibility,
            'in_scope': scope.in_scope,
        }
    return _scope_format


@pytest.fixture
def company_format():
    """Формат Company."""
    def _company_format(company: Company):
        return {
            'id': company.pk,
            'name': company.name,
            'description': company.description,
            'private': company.private,
        }
    return _company_format


@pytest.fixture
def stage_pass_history_format():
    """Формат StagePassHistory."""
    def _stage_pass_history_format(stage_pass_history: StagePassHistory):
        return {
            'id': stage_pass_history.pk,
            'stage_from': stage_pass_history.stage_from,
            'stage_to': stage_pass_history.stage_to,
            'report': stage_pass_history.report,
            'date': stage_pass_history.date,
        }
    return _stage_pass_history_format
