# Generated by Django 5.0.4 on 2024-04-11 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0008_bookingdb_cartdb_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingdb',
            name='time',
        ),
        migrations.AddField(
            model_name='bookingdb',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]