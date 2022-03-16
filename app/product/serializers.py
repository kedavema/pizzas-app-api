from product.models import Category, Ingredient, Pizza
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category objects"""
    name = serializers.CharField(required=True)

    class Meta:
        model = Category
        fields = ('id', 'name',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for ingredient objects"""
    name = serializers.CharField(required=True)
    category = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all(),
        allow_null=False,
        required=True
    )

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'category',)


class PizzaSerializer(serializers.ModelSerializer):
    """Serializer fot the Pizza object"""
    name = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True)
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all(),
        allow_null=False,
        allow_empty=False,
        required=True
    )

    class Meta:
        model = Pizza
        fields = ('id', 'name', 'price', 'ingredients',)
