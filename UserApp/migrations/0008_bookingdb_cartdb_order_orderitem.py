# Generated by Django 5.0.4 on 2024-04-11 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0007_customer_age_customer_mobile'),
        ('VendorApp', '0011_remove_food_vendor_name_food_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('age', models.CharField(max_length=100, null=True)),
                ('mobile_number', models.EmailField(max_length=200)),
                ('email', models.CharField(max_length=255)),
                ('time', models.TimeField(blank=True)),
                ('train_number', models.IntegerField(blank=True, null=True)),
                ('compartment_number', models.IntegerField(blank=True, null=True)),
                ('seat_number', models.IntegerField(blank=True, null=True)),
                ('deliver_station', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('tprice', models.IntegerField(blank=True, null=True)),
                ('food', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='VendorApp.food')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=100, null=True)),
                ('total_price', models.IntegerField(blank=True, null=True)),
                ('shipping', models.IntegerField(blank=True, null=True)),
                ('grand_total', models.IntegerField(blank=True, null=True)),
                ('amount_to_be_paid', models.IntegerField(blank=True, null=True)),
                ('payment_method', models.CharField(max_length=50)),
                ('order_status', models.CharField(choices=[('Order Confirmed', 'Order Confirmed'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Order Confirmed', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.CharField(max_length=100, unique=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.bookingdb')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='Images')),
                ('food_name', models.CharField(blank=True, max_length=30, null=True)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('total_price', models.IntegerField(null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.order')),
            ],
        ),
    ]
