from django.contrib.postgres.fields import ArrayField
from django.db import models


class Travel(models.Model):
    name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    stops = ArrayField(
        models.CharField(max_length=100),
        size=8)

    def __str__(self):
        return self.name
