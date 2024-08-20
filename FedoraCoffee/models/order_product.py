from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .order_extra import Order_extra
from .order import Order
from .product import Product

class Order_product(models.Model):
    quantity = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    note = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(blank=True, max_digits=7, decimal_places=2, default=0)
    extra = models.ManyToManyField(
        Order_extra, related_name="order_products", blank=True
    )
    order = models.ForeignKey(
        Order, on_delete=models.PROTECT, related_name="order_products", blank=False
    )
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="order_products", blank=False
    )

    def __str__(self):
        return f'{self.id} - {self.product} - {self.quantity} unidades'
