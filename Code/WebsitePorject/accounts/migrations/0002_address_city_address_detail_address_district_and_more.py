# Generated by Django 4.2.7 on 2024-03-21 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="city",
            field=models.CharField(blank=True, default="", max_length=25),
        ),
        migrations.AddField(
            model_name="address",
            name="detail",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
        migrations.AddField(
            model_name="address",
            name="district",
            field=models.CharField(blank=True, default="", max_length=25),
        ),
        migrations.AddField(
            model_name="address",
            name="province",
            field=models.CharField(blank=True, default="", max_length=25),
        ),
        migrations.AddField(
            model_name="shop",
            name="city",
            field=models.CharField(blank=True, default="", max_length=25),
        ),
        migrations.AddField(
            model_name="shop",
            name="detail",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
        migrations.AddField(
            model_name="shop",
            name="district",
            field=models.CharField(blank=True, default="", max_length=25),
        ),
        migrations.AddField(
            model_name="shop",
            name="province",
            field=models.CharField(blank=True, default="", max_length=25),
        ),
        migrations.AlterField(
            model_name="address",
            name="address_line",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="shop",
            name="address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
