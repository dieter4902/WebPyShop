# Generated by Django 3.1.4 on 2020-12-18 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shoppingcart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingcart',
            old_name='last_updated',
            new_name='timestamp',
        ),
    ]
