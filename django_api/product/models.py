from django.db import models

from category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)

    class Meta:
        db_table = "product"
        ordering = ['id']
        verbose_name_plural = "Products"
    
    def __str__(self):
        return self.name
