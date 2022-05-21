from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from rules.contrib.models import RulesModelBase, RulesModelMixin


class Recommendation(RulesModelMixin, models.Model, metaclass=RulesModelBase):
    """Рекомендация к пройденному опросу."""

    quiz = models.OneToOneField('Quiz', on_delete=models.CASCADE)
    match = models.PositiveIntegerField(
        _('процент совпадения с ключами ответов'),
    )
    quiz_key = models.ForeignKey('QuizKey', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(
        _('время получения рекомендации'),
        default=datetime.now,
    )
    read = models.BooleanField(
        _('статус рекомендации'),
        default=False,
        null=True,
    )

    class Meta(object):
        verbose_name = _('рекомендация')
        verbose_name_plural = _('рекомендации')

    def __str__(self):
        return f'{self.quiz}-{self.created_at}'
