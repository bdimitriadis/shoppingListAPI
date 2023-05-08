from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Category, Product, ShoppingList, ShoppingListProduct
from core.permissions import IsShoppingListOwner, IsProductInOwnerShoppingLists
from core.serializers import CategorySerializer, ProductSerializer, ShoppingListSerializer, OwnerSerializer, \
    ShoppingListProductSerializer, SignupSerializer, LoginSerializer


class SignupAPIView(APIView):
    """This api will handle signup"""
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'status': status.HTTP_201_CREATED }
            return Response(res, status=status.HTTP_201_CREATED)
        res = {'status': status.HTTP_400_BAD_REQUEST, 'data': serializer.errors}
        return Response(res, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    """This api will handle login and return token for authenticate user."""
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                """We are retrieving the token for authenticated user."""
                token = Token.objects.get(user=user)
                response = {
                       "status": status.HTTP_200_OK,
                       "message": "success",
                       "data": {
                               "Token": token.key
                               }
                       }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                       "status": status.HTTP_401_UNAUTHORIZED,
                       "message": "Invalid Email or Password",
                       }
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        response = {
             "status": status.HTTP_400_BAD_REQUEST,
             "message": "bad request",
             "data": serializer.errors
             }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class OwnerDetail(RetrieveUpdateDestroyAPIView):
    """ The owner view class
    """
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = OwnerSerializer


class OwnerList(ListCreateAPIView):
    """ The owner list view class
    """
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = OwnerSerializer


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    """ The category view class
    """
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryList(ListCreateAPIView):
    """ The category list view class
    """
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    """ The product view class
    """
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductList(ListCreateAPIView):
    """ The product list view class
    """
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShoppingListProductDetail(RetrieveUpdateDestroyAPIView):
    """ The shopping list record view class
    """
    permission_classes = [IsAuthenticated, IsProductInOwnerShoppingLists]
    queryset = ShoppingListProduct.objects.all()
    serializer_class = ShoppingListProductSerializer


class ShoppingListProductListing(ListCreateAPIView):
    """ The shopping-list-records view class
    """
    permission_classes = [IsAuthenticated, IsProductInOwnerShoppingLists]
    queryset = ShoppingListProduct.objects.all()
    serializer_class = ShoppingListProductSerializer


class ShoppingListDetail(RetrieveUpdateDestroyAPIView):
    """ The shopping list view class
    """
    permission_classes = [IsAuthenticated, IsShoppingListOwner]
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer


class ShoppingListListing(ListCreateAPIView):
    """ The shopping-list list view class
    """
    permission_classes = [IsAuthenticated, IsShoppingListOwner]
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
