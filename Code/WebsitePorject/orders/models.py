from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from accounts.models import Customer, Merchant, Shop
from merchants.models import Product

# Create your models here.


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='orders')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='orders', null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    sale_time = models.DateTimeField(default=datetime.now)  # 购买时间
    address_line = models.CharField(max_length=255,default=False)  # customer address
    payment_status = models.BooleanField(default=False)  # 支付状态，默认为未支付
    delivery_status = models.BooleanField(default=False)  # 送达状态，默认为未送达
    isComment = models.BooleanField(default=False)  # 订单是否评论状态

    def save(self, *args, **kwargs):
        # 自动计算订单总价
        self.total_price = sum([item.product_price * item.quantity for item in self.orderitems.all()])
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    product_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    quantity = models.IntegerField(validators=[MinValueValidator(1)])  # 订单数量不能少于1
