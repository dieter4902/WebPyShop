# Generated by Django 4.0.5 on 2022-07-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Useradmin', '0002_myuser_favourite_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='profile_pictures/'),
        ),
    ]