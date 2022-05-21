import re
from datetime import datetime

import deal
from django.db import models
from django.utils.translation import gettext_lazy as _
from rules.contrib.models import RulesModelBase, RulesModelMixin

from nova_quiz.models.quiz_key import QuizKey
from nova_quiz.models.quiz_step import QuizStep
from nova_quiz.models.recommendation import Recommendation


class Quiz(RulesModelMixin, models.Model, metaclass=RulesModelBase):
    """Опрос. Совокупность ответов."""

    started_at = models.DateTimeField(_('начало опроса'), default=datetime.now)

    class Meta(object):
        verbose_name = _('опрос')
        verbose_name_plural = _('опросы')

    def __str__(self):
        return f'Quiz ({self.pk})'

    @deal.post(lambda ans: 0 <= ans <= 100)
    def quiz_key_score(self, quiz_key: QuizKey) -> int:
        """Вычисление процентов совпадения QuizKey с ответами."""
        steps = QuizStep.objects.filter(quiz=self)
        score = 0

        for element in quiz_key.elements.all():
            try:
                step = steps.get(question__tag=element.question_tag)
            except QuizStep.DoesNotExist:
                continue
            answer_index = 0 if step.answer is None else step.answer.index
            if re.match(element.etalon, f'{answer_index}'):
                score += 1

        if quiz_key.elements.count() == 0:
            return 0
        return int(score / quiz_key.elements.count() * 100)

    def computation_recommendation(self) -> dict:
        """Вычисление ответа (рекомендации) для опроса.

        Каждому ответу (QuizKey) ставится в соответствие
        процент попадания в ответ.
        """
        rating = [
            {
                'match': self.quiz_key_score(quiz_key),
                'quiz_key': quiz_key,
            } for quiz_key in QuizKey.objects.all()
        ]

        if not rating:
            quiz_key_for_rec, created = QuizKey.objects.get_or_create(
                title='Отсутствуют данные',
                text='База данных не заполнена. Обратитесь в поддержку.',
            )
            return Recommendation.objects.get_or_create(
                match=0,
                quiz=self,
                quiz_key=quiz_key_for_rec,
            )

        rating.sort(key=lambda percent: percent['match'], reverse=True)

        top_rated = rating[0]
        return Recommendation.objects.get_or_create(
            match=top_rated['match'],
            quiz=self,
            quiz_key=top_rated['quiz_key'],
        )
