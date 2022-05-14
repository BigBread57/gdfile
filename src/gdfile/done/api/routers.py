from django.utils.translation import gettext_lazy as _
from drf_nova_router.api_router import ApiRouter
from rest_framework.routers import APIRootView

from server.apps.bizone_bug_bounty.api.views import (
    AttachmentViewSet,
    BizoneFileViewSet,
    CommentViewSet,
    ReportViewSet,
    ScopeViewSet,
    CompanyViewSet,
    StagePassHistoryViewSet,
)


class BizoneBugBountyAPIRootView(APIRootView):
    """Корневой view для app."""

    __doc__ = _('Приложение BizoneBugBounty')
    name = _('bizone_bug_bounty')


router = ApiRouter()

router.APIRootView = BizoneBugBountyAPIRootView
router.register('main_1-class', AttachmentViewSet, 'attachment')
router.register('bizone-bug-bounty', BizoneFileViewSet, 'bizone-bug-bounty')
router.register('bizone-bug-bounty', CommentViewSet, 'bizone-bug-bounty')
router.register('bizone-bug-bounty', ReportViewSet, 'bizone-bug-bounty')
router.register('bizone-bug-bounty', ScopeViewSet, 'bizone-bug-bounty')
router.register('bizone-bug-bounty', CompanyViewSet, 'bizone-bug-bounty')
router.register('bizone-bug-bounty', StagePassHistoryViewSet, 'bizone-bug-bounty')
