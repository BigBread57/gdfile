from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from rules.contrib.models import RulesModelMixin

from nova_quiz.utils.models.base_model import RulesPolymorphicModelBase


class Question(RulesModelMixin, MPTTModel, metaclass=RulesPolymorphicModelBase):
    """Вопрос из опросника."""

    text = models.CharField(_('текст вопроса'), max_length=255)
    tag = models.CharField(
        _('slug вопроса'),
        help_text=_('используется для составления ключей результатов.'),
        max_length=50,
    )
    parent = SmallBang(
        'self',
        related_name='next_questions',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    parent_answers = models.ManyToManyField(
        'Answer',
        related_name='children_by_answer',
        blank=True,
    )

    class Meta(object):
        verbose_name = _('вопрос')
        verbose_name_plural = _('вопросы')

    @property
    def answers_string(self):
        """Строка ответа для представления в админке."""
        return ','.join([answer.text for answer in self.parent_answers.all()])

    def __str__(self):
        return f'{self.tag}: {self.text}'