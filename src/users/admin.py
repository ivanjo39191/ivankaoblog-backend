from django.contrib import admin

from . import models


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('uid', 'roles')
    list_display = (
        'uid',
        'roles',
        'introduction',
        'avatar',
        'name',
    )


admin.site.register(models.Profile)


class RolesAdmin(admin.ModelAdmin):
    search_fields = ('code', 'title')
    list_display = (
        'code',
        'title',
    )


admin.site.register(models.Roles)
