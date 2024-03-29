# Generated by Django 4.0.6 on 2022-07-27 06:56

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0008_alter_comment_rating_alter_product_hoehlen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=colorfield.fields.ColorField(choices=[('#FFFFFF', 'white'), ('#000000', 'black'), ('#696969', 'gray'), ('#A67133', 'brown'), ('#FF0000', 'red'), ('#FF8C00', 'orange'), ('#FFFF00', 'yellow'), ('#228B22', 'green'), ('#00FFFF', 'cyan'), ('#00BFFF', 'blue'), ('#8A2BE2', 'purple'), ('#FF00FF', 'pink')], default='#000000', image_field=None, max_length=18, samples=None),
        ),
    ]
