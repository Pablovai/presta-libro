# Generated by Django 4.1.7 on 2023-03-20 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlibros', '0005_alter_product_cantidad_paginas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='puntuacion',
            field=models.FloatField(blank=True),
        ),
    ]
