from django.db import models
from django.contrib.auth.models import User


class JerseyPost(models.Model):

    photo = models.CharField(max_length=1000)
    year = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    team = models.ForeignKey("Team", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
