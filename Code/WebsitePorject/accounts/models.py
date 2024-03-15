from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.
'''
Function list:
1. log in/out
2. register
'''


class Customer(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)


class Merchant(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    shop = models.ForeignKey('Shop', on_delete=models.SET_NULL, null=True, related_name='merchants')


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')
    address_line = models.CharField(max_length=255)


class ShoppingCart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='shopping_carts')
    quantity = models.IntegerField(validators=[MaxValueValidator(100)])


class Shop(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='shops')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255) # 默认为空
    total_rating = models.DecimalField(max_digits=3, decimal_places=1) # 默认为0
    image_path = models.CharField(max_length=255) # 存储在硬盘中的路径


class Favorite(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='favorites')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'shop')
