# Generated by Django 4.2.7 on 2024-04-15 14:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitem",
            name="quantity",
            field=models.IntegerField(
                default=1, validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
    ]
