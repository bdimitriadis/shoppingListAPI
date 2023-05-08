from django.contrib import admin
from core.models import Category, Product, ShoppingList, ShoppingListProduct
from rest_framework.authtoken.models import Token


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ShoppingList)
admin.site.register(ShoppingListProduct)
admin.site.register(Token)
# admin.site.register(Owner)
