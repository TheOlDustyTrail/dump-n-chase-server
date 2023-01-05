from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=250)
    bio = models.CharField(max_length=3000)
    logo = models.CharField(max_length=3000)
    carousel1 = models.CharField(max_length=3000)
    carousel2 = models.CharField(max_length=3000)
    carousel3 = models.CharField(max_length=3000)
