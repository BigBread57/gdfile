from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel
from rules.contrib.models import RulesModelMixin

from nova_quiz.models import Question
from nova_quiz.utils.models.base_model import RulesPolymorphicModelBase


class QuizStep(RulesModelMixin, MPTTModel, metaclass=RulesPolymorphicModelBase):
    """Шаг опроса (фактически - ответ на вопрос)."""

    question = models.ForeignKey(
        Question,
        verbose_name=_('вопрос'),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    answer = models.ForeignKey(
        'Answer',
        verbose_name=_('выбранный ответ'),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(_('время ответа'), default=datetime.now)
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_('предыдущий ответ'),
    )
    quiz = models.ForeignKey(
        'Quiz',
        on_delete=models.CASCADE,
        verbose_name=_('опрос'),
    )

    class Meta(object):
        verbose_name = _('ответ на вопрос')
        verbose_name_plural = _('ответы на вопросы')

    def __str__(self):
        if self.answer is None:
            representation = 'без ответа'
        else:
            text = self.answer.text
            index = self.answer.index
            representation = f'{text} ({index})'
        return f'{self.quiz}: {self.question} -> {representation}'
