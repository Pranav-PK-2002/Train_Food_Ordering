# Generated by Django 5.0.4 on 2024-04-13 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UserApp", "0010_food_review_db_vendor_review_db"),
        ("VendorApp", "0017_rename_name_food_single_single_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="d",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="signup_db",
            name="is_approved",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="bookingdb",
            name="compartment_number",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="bookingdb",
            name="seat_number",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="bookingdb",
            name="train_number",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="cartdb",
            name="food",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cart_items",
                to="VendorApp.food_single",
            ),
        ),
    ]
