from django.db import models
from django.utils.translation import gettext_lazy as _
from rules.contrib.models import RulesModelBase, RulesModelMixin


class Answer(RulesModelMixin, models.Model, metaclass=RulesModelBase):
    """Вариант ответа на вопрос."""

    question = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE,
        related_name='answers',
    )
    text = models.CharField(
        _('текст ответа'),
        max_length=255,
        help_text=_('текст, который отображается пользователю'),
    )
    index = models.PositiveIntegerField(
        _('номер ответа'),
        help_text=_('используется для поиска результата опроса.'),
    )

    class Meta(object):
        verbose_name = _('вариант ответа')
        verbose_name_plural = _('варианты ответа')

    def __str__(self):
        return '{tag}_{index}: {text}'.format(
            tag=self.question.tag,
            index=self.index,
            text=self.text,
        )
