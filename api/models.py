from __future__ import unicode_literals
from django.db import models


class User(models.Model):
    player_id = models.CharField(max_length=250, null=True)
    name = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)
    password = models.CharField(max_length=250, null=True)
    phone_no = models.CharField(max_length=250, null=True)
    dob = models.CharField(max_length=250, null=True)
    address = models.CharField(max_length=250, null=True)
    special_skill = models.CharField(max_length=250, null=True)
    fav_game = models.CharField(max_length=250, null=True)
    profile = models.ImageField(max_length=250, null=True)

    def __str__(self):
        return str(self.id)
