# Generated by Django 4.0.5 on 2022-07-28 16:31

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0017_remove_product_hoehlen_remove_product_material_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_file',
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=colorfield.fields.ColorField(choices=[('#FFFFFF', 'White'), ('#000000', 'Black'), ('#696969', 'Gray'), ('#A67133', 'Brown'), ('#FF0000', 'Red'), ('#FF8C00', 'Orange'), ('#FFFF00', 'Yellow'), ('#228B22', 'Green'), ('#00FFFF', 'Cyan'), ('#00BFFF', 'Blue'), ('#8A2BE2', 'Purple'), ('#FF00FF', 'Pink')], default='#000000', image_field=None, max_length=18, samples=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_picture',
            field=models.ImageField(blank=True, null=True, upload_to='product_pictures/'),
        ),
    ]