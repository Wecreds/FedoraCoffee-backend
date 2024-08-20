from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .extra import Extra

class Order_extra(models.Model):
    quantity = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    extra = models.ForeignKey(
        Extra, on_delete=models.PROTECT, related_name="order_extras", blank=False
    )
    
    def __str__(self):
        return self.extra