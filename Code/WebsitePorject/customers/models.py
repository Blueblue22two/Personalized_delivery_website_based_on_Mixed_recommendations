from django.db import models
from accounts.models import Customer
from merchants.models import Product

# FavItems Model
class FavItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='fav_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favored_by')

    class Meta:
        unique_together = ('customer', 'product')
        verbose_name = 'Favorite Item'
        verbose_name_plural = 'Favorite Items'

# Comments Model
class Comment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[models.MinValueValidator(0), models.MaxValueValidator(5)])

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
