from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from accounts.models import Merchant, Shop


# Create your models here.


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    category = models.CharField(max_length=255, blank=True)  # Blank allowed for category
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                         validators=[MinValueValidator(0)])
    discount_time = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)
    image_path = models.CharField(max_length=255, blank=True)  # Assuming image path could be blank
    average_rate = models.DecimalField(max_digits=3, decimal_places=1, default=0)  # Added field


class ShopRating(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='ratings')
    rate = models.DecimalField(max_digits=3, decimal_places=1, default=0,
                               validators=[MinValueValidator(0), MaxValueValidator(5)])  # rate ranges from 0 to 5

    class Meta:
        # Ensure that a shop can be rated only once by a specific entity (prevent duplicate ratings).
        unique_together = ('shop', 'id')
