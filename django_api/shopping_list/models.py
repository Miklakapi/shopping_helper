from django.db import models

# Create your models here.
class ShoppingList(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    owner = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "shopping_list"
