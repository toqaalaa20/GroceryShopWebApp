# Generated by Django 4.2.8 on 2023-12-19 06:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("GroceryApp", "0004_product_reviews"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="product_reviews",
            new_name="ProductReviews",
        ),
    ]
