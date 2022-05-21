from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "categories"
        ordering = ['id']
    
    def __str__(self):
        return self.name
