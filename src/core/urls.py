from django.urls import path

from core.views import CategoryList, CategoryDetail, ProductDetail, ProductList, ShoppingListDetail, \
    ShoppingListListing, OwnerDetail, OwnerList, ShoppingListProductListing, ShoppingListProductDetail

app_name = 'core'

urlpatterns = [
    path('owners/<int:pk>', OwnerDetail.as_view()),
    path('owners/', OwnerList.as_view()),
    path('categories/<int:pk>', CategoryDetail.as_view()),
    path('categories/', CategoryList.as_view()),
    path('slproducts/<int:pk>', ShoppingListProductDetail.as_view()),
    path('slproducts/', ShoppingListProductListing.as_view()),
    path('products/<int:pk>', ProductDetail.as_view()),
    path('products/', ProductList.as_view()),
    path('shopping-lists/<int:pk>', ShoppingListDetail.as_view()),
    path('shopping-lists/', ShoppingListListing.as_view()),
]
