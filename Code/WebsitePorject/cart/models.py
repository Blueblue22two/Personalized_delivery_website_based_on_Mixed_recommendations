from django.db import models

from accounts.models import ShoppingCart
from merchants.models import Product
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(quantity__gt=0), name='quantity_gt_0'),
        ]
