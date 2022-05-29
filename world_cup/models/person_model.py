from django.db import models

from .base_model import BaseModel
from .team_model import Team


class Person(BaseModel):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birth_date = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.PROTECT)

    class Meta:
        abstract = True