from django.db import models
from django.db.models import (
    Count,
    Q,
    Avg,
    F,
    FloatField,
    ExpressionWrapper,
)
from django.db.models.functions import Cast, Now

from . import Team
from .person_model import Person


class PlayerManager(models.Manager):
    def get_youngest(self):
        return self.all().order_by('-birth_date').first()

    def get_oldest(self):
        return self.all().order_by('birth_date').first()

    def count_not_first_team(self):
        return self.filter(is_first_team=False).count()

    def calculate_average_not_first_team_by_team(self):
        value = self.values('team__name'). \
            annotate(
                average_not_first_team=Cast(
                    Count('id', Q(is_first_team=False)),
                    FloatField()
                ) / Cast(
                    Count('id'),
                    FloatField()
                )
        )
        return value

    def calculate_team_with_more_players(self):
        value = self.values('team__name'). \
            annotate(
                count_players=Count('id')
        ).order_by('-count_players')
        return value.first()

    def calculate_average_age(self):
        value = self.annotate(
            age=(ExpressionWrapper(Now() - F('birth_date'), output_field=models.DurationField()))
        ).aggregate(
            average_age=Avg('age')
        )
        if value:
            return value.get('average_age').total_seconds() / 60 / 60 / 24 / 365.25
        return None

    def calcule_average_count_players_by_team(self):
        value = self.values('team__name'). \
            annotate(
                count=Count('id')
        ).aggregate(
            average_count_player=Avg('count')
        )
        return value.get('average_count_player')


class Positions(models.TextChoices):
    FORWARD = 'Forward'
    MIDFIELDER = 'Midfielder'
    DEFENDER = 'Defender'
    GOALKEEPER = 'Goalkeeper'


class Player(Person):

    photo = models.CharField(max_length=1000)
    position = models.CharField(
        max_length=20,
        choices=Positions.choices
    )
    player_number = models.IntegerField()
    is_first_team = models.BooleanField()
    team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='players')

    objects = PlayerManager()

    def __str__(self):
        return f'{self.name} {self.lastname} ({self.player_number})'

    class Meta:
        db_table = 'player'
