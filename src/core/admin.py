from django.contrib import admin
from core.models import Category, Owner, Product, ShoppingList, ShoppingListProduct


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ShoppingList)
admin.site.register(ShoppingListProduct)
admin.site.register(Owner)
