from django.contrib import admin

from ..models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'flag_image',
        'shield_image',
    )


admin.site.register(Team, TeamAdmin)
