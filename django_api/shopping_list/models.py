from django.db import models
from django.contrib.auth.models import User


class ShoppingList(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "shopping_list"
        ordering = ['-id']
        verbose_name_plural = "Shopping list"

    def __str__(self):
        return self.name
