from django.contrib import admin
from .models import MyUser
from Product.models import Product

# Register your models here.

admin.site.register(MyUser)
admin.site.register(Product)
