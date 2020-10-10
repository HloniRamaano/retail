from django.contrib import admin
from . models import Product, ShoppingCart,Payment

admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(Payment)

