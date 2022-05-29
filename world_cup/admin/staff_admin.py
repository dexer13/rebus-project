from django.contrib import admin

from ..models import Staff


class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'lastname',
        'birth_date',
        'team',
        'nationality',
        'rol',
    )


admin.site.register(Staff, StaffAdmin)
