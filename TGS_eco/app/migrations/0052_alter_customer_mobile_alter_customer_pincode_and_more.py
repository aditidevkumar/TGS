# Generated by Django 5.1.2 on 2024-10-26 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0051_alter_customer_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='customer',
            name='pincode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[], max_length=50),
        ),
    ]
