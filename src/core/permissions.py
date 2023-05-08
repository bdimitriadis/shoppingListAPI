from rest_framework import permissions
from core.models import ShoppingList


class IsShoppingListOwner(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    # for object level permissions
    def has_object_permission(self, request, view, shopping_list):
        return shopping_list.owner.id == request.user.id


class IsProductInOwnerShoppingLists(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    # for object level permissions
    def has_object_permission(self, request, view, shopping_list_product):
        sl_owners = list(map(lambda sl: sl.owner, shopping_list_product.shopping_lists))
        return request.user.id in sl_owners

