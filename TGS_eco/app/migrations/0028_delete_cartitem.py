# Generated by Django 5.1.2 on 2024-10-13 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_remove_customer_product_cart_cartitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
