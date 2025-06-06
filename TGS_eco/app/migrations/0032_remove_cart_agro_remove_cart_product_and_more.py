# Generated by Django 5.1.2 on 2024-10-15 13:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_cart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='agro',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='seed',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='soil',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='tool',
        ),
        migrations.AddField(
            model_name='cart',
            name='agros',
            field=models.ManyToManyField(blank=True, to='app.agro'),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='app.product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='seeds',
            field=models.ManyToManyField(blank=True, to='app.seed'),
        ),
        migrations.AddField(
            model_name='cart',
            name='soils',
            field=models.ManyToManyField(blank=True, to='app.soil'),
        ),
        migrations.AddField(
            model_name='cart',
            name='tools',
            field=models.ManyToManyField(blank=True, to='app.tool'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
