# Generated by Django 4.2.8 on 2023-12-21 16:36

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):
    dependencies = [
        ("GroceryApp", "0009_rename_id_cartorder_ct_ord_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartorderitems",
            name="invoice_number",
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet="abcdefgh12345",
                length=10,
                max_length=20,
                null=True,
                prefix="",
                unique=True,
            ),
        ),
    ]
