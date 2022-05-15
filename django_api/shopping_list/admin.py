from django.contrib import admin
from .models import ShoppingList

# Register your models here.
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity', 'owner', 'date')

admin.site.register(ShoppingList, ShoppingListAdmin)