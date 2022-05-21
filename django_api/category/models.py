from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "category"
        ordering = ['id']
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
