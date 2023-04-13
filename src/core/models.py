from django.db import models


class Owner(models.Model):
    """ The owner of each shopping list
    """
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    """ The category where each product belongs to
    """
    name = models.CharField(max_length=50, unique=True)
    icon = models.CharField(max_length=50)  # The name of the category icon

    def __str__(self):
        return self.name


class Product(models.Model):
    """ The product contained in a shopping list
    """
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ShoppingListProduct(models.Model):
    """ Record with the details about the specific product in a specific shopping list,
    regarding amounts and prices
    """

    product = models.ForeignKey('Product', related_name='shopping_list_products', on_delete=models.CASCADE)
    price = models.FloatField(null=True)
    price_unit = models.CharField(max_length=10, null=True)
    amount = models.FloatField(null=True)
    amount_unit = models.CharField(max_length=10, null=True)
    checked = models.BooleanField(default=False, null=True)

    class Meta:
        db_table = 'shopping_list_product'
        constraints = [
            models.UniqueConstraint(fields=['product', 'price', 'price_unit', 'amount', 'amount_unit'],
                                    name='unique_shopping_list_product')
        ]


class ShoppingList(models.Model):
    """ The shopping list containing the various products for an owner
    """

    name = models.CharField(max_length=50, unique=True)
    shopping_list_products = models.ManyToManyField('ShoppingListProduct', related_name='shopping_lists')
    owner = models.ForeignKey(Owner, related_name='owned_shopping_lists', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
