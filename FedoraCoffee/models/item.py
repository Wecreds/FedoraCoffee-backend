from django.db import models

class Item(models.Model):
    description = models.CharField(max_length=75)
    unity_of_measure = models.CharField(max_length=20)
    stock = models.IntegerField(default=0)
    minimum_stock = models.IntegerField(default=0)

    def __str__(self):
        return self.description