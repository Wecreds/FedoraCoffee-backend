from django.contrib import admin
from FedoraCoffee import models

admin.site.register(models.Client)
admin.site.register(models.Order)
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Item)
admin.site.register(models.Extra)
admin.site.register(models.Order_extra)
admin.site.register(models.Order_product)

# Register your models here.
