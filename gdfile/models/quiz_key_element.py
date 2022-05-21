from django.db import models
from django.utils.translation import gettext_lazy as _
from rules.contrib.models import RulesModelBase, RulesModelMixin


class QuizKeyElement(RulesModelMixin, models.Model, metaclass=RulesModelBase):
    """Элемент заключения (ответ и его 'правильные' варианты)."""

    quiz_key = models.ForeignKey(
        'QuizKey',
        verbose_name=_('заключение'),
        help_text=_('частью какого заключения является этот элемент'),
        on_delete=models.CASCADE,
        related_name='elements',
    )
    question_tag = models.CharField(_('тэг вопроса'), max_length=50)
    etalon = models.CharField(
        _('регулярное выражение соответствия ответа'),
        help_text=_(
            'если регулярное выражение совпадает с ответом - ' +
            'ответ считается правильным',
        ),
        max_length=100,
    )

    class Meta(object):
        verbose_name = _('заключение. элемент')
        verbose_name_plural = _('заключение. элементы')

    def __str__(self):
        return f'{self.quiz_key}, {self.question_tag}: {self.etalon}'
