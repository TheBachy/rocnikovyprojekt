from django.contrib import admin

from django.contrib import admin
from .models import *

admin.site.register(Players)
admin.site.register(PlayersHasReplay)
admin.site.register(Replay)
admin.site.register(ReplayHasTeams)
admin.site.register(Teams)

# Register your models here.
