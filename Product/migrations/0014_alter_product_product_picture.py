# Generated by Django 4.0.5 on 2022-07-28 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0013_alter_product_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_picture',
            field=models.ImageField(blank=True, upload_to='product_pictures/'),
        ),
    ]
