from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=250)
    bio = models.CharField(max_length=3000)
