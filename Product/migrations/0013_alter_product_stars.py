# Generated by Django 4.0.6 on 2022-07-28 00:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0012_alter_product_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stars',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]