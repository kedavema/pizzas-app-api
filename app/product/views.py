from drf_yasg.utils import swagger_auto_schema
from product.models import Category, Ingredient, Pizza
from product.serializers import (CategorySerializer, IngredientSerializer,
                                 PizzaSerializer)
from product.utils import resource_checker
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

############################## Endpoints of Pizzas #################################


class PizzasAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(responses={200: PizzaSerializer(many=True)})
    def get(self, request, format=None):
        """Return a list of Pizza objects"""
        if request.user.is_superuser:
            pizzas = Pizza.objects.all()
            serializer = PizzaSerializer(pizzas, many=True)
            return Response(serializer.data)
        else:
            pizzas = Pizza.objects.all().filter(is_active=True)
            serializer = PizzaSerializer(pizzas, many=True)
            return Response(serializer.data)

    @swagger_auto_schema(responses={201: PizzaSerializer()})
    def post(self, request, format=None):
        """Create a new pizza object"""
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PizzaDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(responses={200: PizzaSerializer()})
    @resource_checker(Pizza)
    def get(self, request, pk, format=None):
        """Get a pizza object by ID"""
        pizza = Pizza.objects.get(pk=pk)
        serializer = PizzaSerializer(pizza)

        return Response(serializer.data)

    @swagger_auto_schema(responses={200: PizzaSerializer()})
    @resource_checker(Pizza)
    def put(self, request, pk, format=None):
        """Update a pizza object"""
        pizza = Pizza.objects.filter(id=pk).first()
        serializer = PizzaSerializer(pizza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'Pizza deleted succesfully'})
    @resource_checker(Pizza)
    def delete(self, request, pk, format=None):
        """Delete a pizza object"""
        pizza = Pizza.objects.filter(id=pk).first()
        pizza.delete()

        return Response(
            {"message": f"Pizza '{pizza}' deleted succesfully"},
            status=status.HTTP_204_NO_CONTENT
        )


class DeleteIngredientPizza(APIView):
    """Delete an ingredient object of a pizza"""
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(responses={204: 'Ingredient of pizza deleted succesfully'})
    def delete(self, request, pizza_id, ingredient_id, format=None):
        pizza = Pizza.objects.get(id=pizza_id)
        ingredient = Ingredient.objects.get(id=ingredient_id)
        pizza.ingredients.remove(ingredient)

        return Response({
            "message": f"Se ha removido el ingrediente {ingredient} de la pizza {pizza}"
        }, status=status.HTTP_204_NO_CONTENT)


############################# Endpoints of Ingredients #############################


class IngredientsAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(responses={200: IngredientSerializer(many=True)})
    def get(self, request, format=None):
        """Return a list of Ingredient objects"""
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(responses={201: IngredientSerializer()})
    def post(self, request, format=None):
        """Create a new Ingredient"""
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IngredientDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(responses={200: IngredientSerializer(many=True)})
    @resource_checker(Ingredient)
    def get(self, request, pk, format=None):
        """Get an ingredient object by ID"""
        ingredient = Ingredient.objects.get(pk=pk)
        serializer = IngredientSerializer(ingredient)

        return Response(serializer.data)

    @swagger_auto_schema(responses={200: IngredientSerializer()})
    @resource_checker(Ingredient)
    def put(self, request, pk, format=None):
        """Update an ingredient object"""
        ingredient = Ingredient.objects.filter(id=pk).first()
        serializer = IngredientSerializer(ingredient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'Ingredient deleted succesfully'})
    @resource_checker(Ingredient)
    def delete(self, request, pk, format=None):
        """Delete an ingredient object"""
        ingredient = Ingredient.objects.filter(id=pk).first()
        pizza_with_that_ingredient = Pizza.objects.filter(
            ingredients=ingredient).exists()
        # If there is a pizza associated with that ingredient, it cannot be deleted
        if pizza_with_that_ingredient:
            return Response(
                {"message": "There is a pizza with that ingredient, it cannot be deleted"}
            )
        else:
            ingredient.delete()
            return Response(
                {"message": f"Ingredient '{ingredient}' deleted succesfully"},
                status=status.HTTP_204_NO_CONTENT
            )


############################# Endpoints of Categories #############################


class CategoriesAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(responses={200: CategorySerializer(many=True)})
    def get(self, request, format=None):
        """Return a list of Category objects"""
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(responses={201: CategorySerializer()})
    def post(self, request, format=None):
        """Create a new category object"""
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(responses={200: CategorySerializer(many=True)})
    @resource_checker(Category)
    def get(self, request, pk, format=None):
        """Get a category object by ID"""
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)

        return Response(serializer.data)

    @swagger_auto_schema(responses={200: CategorySerializer()})
    @resource_checker(Category)
    def put(self, request, pk, format=None):
        """Update a category object"""
        category = Category.objects.filter(id=pk).first()
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'Category deleted succesfully'})
    @resource_checker(Category)
    def delete(self, request, pk, format=None):
        """Delete a category object"""
        category = Category.objects.filter(id=pk).first()
        category.delete()

        return Response(
            {"message": f"Category '{category}' deleted succesfully"},
            status=status.HTTP_204_NO_CONTENT
        )
