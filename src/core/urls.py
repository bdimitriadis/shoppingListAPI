from django.urls import path

from core.views import CategoryList, CategoryDetail, ProductDetail, ProductList, ShoppingListDetail, \
    ShoppingListListing, OwnerDetail, OwnerList, ShoppingListProductListing, ShoppingListProductDetail, SignupAPIView, \
    LoginAPIView

app_name = 'core'

urlpatterns = [
    path("signup/", SignupAPIView.as_view(), name="owner-signup"),
    path("login/", LoginAPIView.as_view(), name="owner-login"),
    path('owners/<int:pk>', OwnerDetail.as_view(), name='owner-detail'),
    path('owners/', OwnerList.as_view(), name='owners-list'),
    path('categories/<int:pk>', CategoryDetail.as_view(), name='category-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('slproducts/<int:pk>', ShoppingListProductDetail.as_view(), name='slproduct-detail'),
    path('slproducts/', ShoppingListProductListing.as_view(), name='slproduct-list'),
    path('products/<int:pk>', ProductDetail.as_view(), name='product-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('shopping-lists/<int:pk>', ShoppingListDetail.as_view(), name='shopping-list-detail'),
    path('shopping-lists/', ShoppingListListing.as_view(), name='shopping-list-listing'),
]
