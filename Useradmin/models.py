from datetime import date, datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from Shoppingcart.models import ShoppingCart


class MyUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    favourite_cat = models.CharField(max_length=100)
    
    def count_shopping_cart_items(self):
        count = 0
        if self.is_authenticated:
            shopping_carts = ShoppingCart.objects.filter(myuser=self)
            if shopping_carts:
                shopping_cart = shopping_carts.first()
                count = shopping_cart.get_number_of_items()

        return count

