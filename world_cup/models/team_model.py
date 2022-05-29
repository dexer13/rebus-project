from django.db import models

from .base_model import BaseModel


class Team(BaseModel):
    name = models.CharField(max_length=100)
    flag_image = models.CharField(max_length=1000)
    shield_image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'team'
