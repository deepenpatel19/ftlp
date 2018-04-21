# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User, HostTournament, Location, Ground
from django.utils.translation import ugettext_lazy


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_no', 'dob', 'address', 'fav_game')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('organizer_first_name', 'tournament_name',  'date', 'player_req', 'ground_name')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)


class GroundAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'available_status', )


admin.site.register(User, UserAdmin)
admin.site.register(HostTournament, TeamAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Ground, GroundAdmin)
admin.site.site_header = ("FTLP")
admin.site.site_title = ("Site Administration")
