# Generated by Django 4.2.7 on 2024-03-23 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0003_remove_order_product_remove_order_product_price_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="isComment",
            field=models.BooleanField(default=False),
        ),
    ]
