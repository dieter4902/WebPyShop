# Generated by Django 4.0.5 on 2022-06-25 19:21

import colorfield.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=colorfield.fields.ColorField(choices=[('#FFFFFF', 'white'), ('#000000', 'black')], default='#000000', image_field=None, max_length=18, samples=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='hoehlen',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(-3)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='length',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='stockwerke',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(-3)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(0)]),
        ),
    ]
