from django.contrib import admin
from .models import ShoppingList


class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity', 'owner', 'date')

admin.site.register(ShoppingList, ShoppingListAdmin)
