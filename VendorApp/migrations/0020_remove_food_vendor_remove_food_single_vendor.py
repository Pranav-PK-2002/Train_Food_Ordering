# Generated by Django 5.0.4 on 2024-04-13 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("VendorApp", "0019_food_single_average_rating"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="food",
            name="vendor",
        ),
        migrations.RemoveField(
            model_name="food_single",
            name="vendor",
        ),
    ]