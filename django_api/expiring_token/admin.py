from django.contrib import admin

from .models import ExpiringToken


class ExpiringTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'created', 'expires',)
    fields = ('user',)
    ordering = ('-expires',)


admin.site.register(ExpiringToken, ExpiringTokenAdmin)
