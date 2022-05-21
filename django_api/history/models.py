from django.db import models
from django.contrib.auth.models import User

from product.models import Product


class History(models.Model):
    quantity = models.IntegerField()
    price = models.FloatField()
    date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)

    class Meta:
        db_table = "history"
        ordering = ['-id']
        verbose_name_plural = "History"
    
    def __str__(self):
        return self.product.name
