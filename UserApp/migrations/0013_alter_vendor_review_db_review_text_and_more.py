# Generated by Django 5.0.4 on 2024-04-13 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UserApp", "0012_remove_orderitem_d"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vendor_review_db",
            name="review_text",
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name="vendor_review_db",
            name="username",
            field=models.TextField(max_length=100),
        ),
    ]