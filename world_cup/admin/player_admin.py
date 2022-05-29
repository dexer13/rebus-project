from django.contrib import admin

from ..models import Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'lastname',
        'birth_date',
        'team',
        'photo',
        'position',
        'player_number',
        'is_first_team',
    )


admin.site.register(Player, PlayerAdmin)
