# Generated by Django 4.0.6 on 2022-07-28 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0025_merge_20220728_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]