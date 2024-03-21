from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from accounts.models import Customer, Merchant
from merchants.models import Product

# Create your models here.
'''
无论一次下单多少，都以一个商品来一个order
'''


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='orders')
    product_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    quantity = models.IntegerField(validators=[MinValueValidator(1)])  # 订单数量不能少于1
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    sale_time = models.DateTimeField(default=datetime.now) # 购买时间
    address_line = models.CharField(max_length=255) # address of customer
    payment_status = models.BooleanField(default=False)  # 添加支付状态字段，默认为未支付
    delivery_status = models.BooleanField(default=False)  # 添加送达状态字段，默认为未送达

    def save(self, *args, **kwargs):
        # 自动计算订单总价
        self.total_price = self.product_price * self.quantity
        super().save(*args, **kwargs)
