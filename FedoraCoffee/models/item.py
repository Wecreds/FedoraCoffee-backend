from django.db import models

class Item(models.Model):
    description = models.CharField(max_length=75)
    UoM = models.CharField(max_length=20)
    stock = models.IntegerField(default=0)
    minStock = models.IntegerField(default=0)

    def __str__(self):
        return self.name