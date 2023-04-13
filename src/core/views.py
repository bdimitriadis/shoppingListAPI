from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from core.models import Category, Product, ShoppingList, Owner, ShoppingListProduct
from core.serializers import CategorySerializer, ProductSerializer, ShoppingListSerializer, OwnerSerializer, \
    ShoppingListProductSerializer


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    """ The category view class
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryList(ListCreateAPIView):
    """ The category list view class
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OwnerDetail(RetrieveUpdateDestroyAPIView):
    """ The owner view class
    """
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class OwnerList(ListCreateAPIView):
    """ The owner list view class
    """
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    """ The product view class
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductList(ListCreateAPIView):
    """ The product list view class
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShoppingListProductDetail(RetrieveUpdateDestroyAPIView):
    """ The shopping list record view class
    """
    queryset = ShoppingListProduct.objects.all()
    serializer_class = ShoppingListProductSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)


class ShoppingListProductListing(ListCreateAPIView):
    """ The shopping-list-records view class
    """
    queryset = ShoppingListProduct.objects.all()
    serializer_class = ShoppingListProductSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)


class ShoppingListDetail(RetrieveUpdateDestroyAPIView):
    """ The shopping list view class
    """
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)


class ShoppingListListing(ListCreateAPIView):
    """ The shopping-list list view class
    """
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)
