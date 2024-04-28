from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from accounts.models import Customer, Merchant, Shop
from merchants.models import Product


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='orders')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='orders', null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    sale_time = models.DateTimeField(default=timezone.now)
    address_line = models.CharField(max_length=255,default='')
    payment_status = models.BooleanField(default=False)
    delivery_status = models.BooleanField(default=False)
    isComment = models.BooleanField(default=False)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    product_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
