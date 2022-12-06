from django.db import models
from django.contrib.auth.models import User


class Like(models.Model):

    jersey = models.ForeignKey("JerseyPost", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
