from rest_framework import serializers

from core.models import Category, Product, ShoppingList, Owner, ShoppingListProduct


class CategorySerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=50)
    # icon = serializers.CharField(max_length=50)

    products = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Category
        fields = ('id', 'name', 'icon', 'products')

    # def create(self, validated_data):
    #     return Category.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.icon = validated_data.get('icon', instance.icon)
    #
    #     instance.save()
    #     return instance


class OwnerSerializer(serializers.ModelSerializer):
    shopping_lists = serializers.RelatedField(source='owned_shopping_lists', many=True, read_only=True)
    # name = serializers.CharField(max_length=50)
    # email = serializers.EmailField()
    #
    # def create(self, validated_data):
    #     return Owner.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.email = validated_data.get('email', instance.email)
    #
    #     instance.save()
    #     return instance

    class Meta:
        model = Owner
        fields = ('id', 'name', 'email', 'shopping_lists')


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category_id = validated_data.get('category_id', instance.category_id)

        instance.save()
        return instance


class ShoppingListProductSerializer(serializers.ModelSerializer):
    shopping_lists = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = ShoppingListProduct
        fields = ('id', 'product', 'price', 'price_unit', 'amount', 'amount_unit', 'checked', 'shopping_lists')


class ShoppingListSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=50)
    shopping_list_products_ids = ShoppingListProductSerializer(many=True, read_only=True)
    # owner_id = OwnerSerializer(many=False, read_only=True)

    # def create(self, validated_data):
    #     return ShoppingList.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.shopping_list_products_ids.set(validated_data.get(
    #         'shopping_list_products_ids', instance.shopping_list_products_ids))
    #     instance.owner_id = validated_data.get('owner_id', instance.owner_id)
    #
    #     instance.save()
    #     return instance
    class Meta:
        model = ShoppingList
        fields = ('id', 'name', 'shopping_list_products_ids', 'owner')
