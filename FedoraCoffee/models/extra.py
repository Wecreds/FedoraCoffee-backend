from django.db import models

class Extra(models.Model):
    description = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.description