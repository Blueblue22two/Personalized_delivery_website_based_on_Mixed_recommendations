from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Address)
admin.site.register(models.ShoppingCart)
admin.site.register(models.Merchant)
admin.site.register(models.Shop)
