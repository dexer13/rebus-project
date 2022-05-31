from django.db import models

from .base_model import BaseModel


class Person(BaseModel):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birth_date = models.DateField()

    class Meta:
        abstract = True
