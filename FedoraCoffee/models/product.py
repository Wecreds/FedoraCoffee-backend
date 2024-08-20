from django.db import models

from .category import Category
from uploader.models import Image

class Product(models.Model):
    name = models.CharField(max_length=75)
    ingredients = models.JSONField() # O Django aponta problema ao tentar nomear um objeto como "models", provavelmente por causa que esse nome é usado em outros lugares.
    price = models.DecimalField(blank=False, max_digits=7, decimal_places=2, default=0)
    photo = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="products", blank=False
    )

    def __str__(self):
        return self.name