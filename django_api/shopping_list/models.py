from django.db import models


class ShoppingList(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    owner = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "shopping_list"
        ordering = ['-id']

    def __str__(self):
        return self.name
