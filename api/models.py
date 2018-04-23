from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)
    password = models.CharField(max_length=250, null=True)
    phone_no = models.CharField(max_length=250, null=True)
    dob = models.CharField(max_length=250, null=True)
    address = models.CharField(max_length=250, null=True)
    special_skill = models.CharField(max_length=250, null=True)
    fav_game = models.CharField(max_length=50, null=True)
    profile = models.ImageField(null=True, upload_to="Images/")
    score_or_prev_game = models.IntegerField(null=True)
    # tournament_rsvp = models.

    def __str__(self):
        return str(self.id)


class Location(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.name)


class Ground(models.Model):
    name = models.CharField(max_length=50, null=True)
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, null=True)
    available_status = models.BooleanField(default=False)
    price = models.FloatField()
    rent_by = models.CharField(max_length=50, null=True)
    date = models.CharField(max_length=50, null=True)
    start_time = models.CharField(max_length=50, null=True)
    end_time = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.name)


class HostTournament(models.Model):
    organizer_first_name = models.CharField(max_length=50, null=True)
    organizer_last_name = models.CharField(max_length=50, null=True)
    tournament_name = models.CharField(max_length=50, null=True)
    date = models.CharField(max_length=50, null=True)
    player_req = models.IntegerField(null=True)
    ground_name = models.CharField(max_length=50, null=True)
    player_rsvp = models.IntegerField(null=True)

    def __str__(self):
        return str(self.tournament_name)
