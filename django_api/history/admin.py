from django.contrib import admin
from .models import History


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'price', 'date', 'owner',)


admin.site.register(History, HistoryAdmin)
