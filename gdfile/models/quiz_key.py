from django.db import models
from django.utils.translation import gettext_lazy as _
from rules.contrib.models import RulesModelBase, RulesModelMixin


class QuizKey(RulesModelMixin, models.Model, metaclass=RulesModelBase):
    """Заключение на ответы пользователя.

    Представляет собой совокупность QuizKeyElement.
    """

    title = models.CharField(_('заголовок'), max_length=255)
    text = models.CharField(_('текст заключения'), max_length=1023)

    class Meta(object):
        verbose_name = _('заключение')
        verbose_name_plural = _('заключения')

    def __str__(self):
        return f'{self.title}'
