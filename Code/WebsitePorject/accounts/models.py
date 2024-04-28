from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Customer(models.Model):
    username = models.CharField(max_length=50, db_index=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11)


class Merchant(models.Model):
    username = models.CharField(max_length=50, db_index=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11)
    shop = models.ForeignKey('Shop', on_delete=models.SET_NULL, null=True, related_name='merchants')


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')
    address_line = models.CharField(max_length=255, null=True, blank=True)
    province = models.CharField(max_length=25, blank=True, default='')
    city = models.CharField(max_length=25, blank=True, default='')
    district = models.CharField(max_length=25, blank=True, default='')
    detail = models.CharField(max_length=100, blank=True, default='')


class ShoppingCart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='shopping_carts')
    quantity = models.IntegerField(validators=[MaxValueValidator(100)])


class Shop(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name='shops')
    name = models.CharField(max_length=255)
    total_rating = models.DecimalField(max_digits=3, decimal_places=1,default=0)
    image_path = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    province = models.CharField(max_length=25, blank=True, null=False, default='')
    city = models.CharField(max_length=25, blank=True, null=False, default='')
    district = models.CharField(max_length=25, blank=True, null=False, default='')
    detail = models.CharField(max_length=100, blank=True, null=False, default='')


class Favorite(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='favorites')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'shop')


# function that automatically creates a ShoppingCart object when a Customer object is created
@receiver(post_save, sender=Customer)
def create_shopping_cart(sender, instance, created, **kwargs):
    if created:
        ShoppingCart.objects.create(customer=instance, quantity=0)
