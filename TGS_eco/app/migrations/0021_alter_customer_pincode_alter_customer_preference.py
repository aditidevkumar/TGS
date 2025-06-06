# Generated by Django 5.1.2 on 2024-10-12 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_category_title_alter_customer_preference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pincode',
            field=models.IntegerField(default=6, max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='preference',
            field=models.ManyToManyField(to='app.category'),
        ),
    ]
