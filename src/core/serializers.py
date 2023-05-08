from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Category, Product, ShoppingList, ShoppingListProduct


class SignupSerializer(serializers.ModelSerializer):
    """override create method to change the password into hash."""

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super(SignupSerializer, self).create(validated_data)

    class Meta:
        model = User
        fields = ['username', 'password']


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Category
        fields = ('id', 'name', 'icon', 'products')


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category_id = validated_data.get('category_id', instance.category_id)

        instance.save()
        return instance


class ShoppingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingList
        fields = ('id', 'name', 'shopping_list_products', 'owner')


class OwnerSerializer(serializers.ModelSerializer):
    shopping_lists = ShoppingListSerializer(source='owned_shopping_lists', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'shopping_lists')


class ShoppingListProductSerializer(serializers.ModelSerializer):
    shopping_lists = ShoppingListSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingListProduct
        fields = ('id', 'product', 'price', 'price_unit', 'amount', 'amount_unit', 'checked', 'shopping_lists')


