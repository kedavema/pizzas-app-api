from rest_framework.views import APIView
from product.models import Pizza, Ingredient, Category
from product.serializers import (
    PizzaSerializer,
    IngredientSerializer,
    CategorySerializer
)
from rest_framework.response import Response
from rest_framework import status
from product.utils import resource_checker
from rest_framework.permissions import IsAuthenticated


############################## Endpoints of Pizzas #################################


class PizzasAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        if request.user.is_superuser:
            pizzas = Pizza.objects.all()
            serializer = PizzaSerializer(pizzas, many=True)
            return Response(serializer.data)
        else:
            pizzas = Pizza.objects.all().filter(is_active=True)
            serializer = PizzaSerializer(pizzas, many=True)
            return Response(serializer.data)
      
    def post(self, request, format=None):
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      

class PizzaDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    @resource_checker(Pizza)
    def get(self, request, pk, format=None):
        pizza = Pizza.objects.get(pk=pk)
        serializer = PizzaSerializer(pizza)
        return Response(serializer.data)

    @resource_checker(Pizza)
    def put(self, request, pk, format=None):
        pizza = Pizza.objects.filter(id=pk).first()
        serializer = PizzaSerializer(pizza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
    @resource_checker(Pizza)
    def delete(self, request, pk, format=None):
        pizza = Pizza.objects.filter(id=pk).first()
        pizza.delete()
        return Response({"message": f"Pizza '{pizza}' deleted succesfully"}, status=status.HTTP_204_NO_CONTENT)
      
      
class DeleteIngredientPizza(APIView):
    """Delete an ingredient of a pizza"""
    permission_classes = (IsAuthenticated,)
    def delete(self, request, pizza_id, ingredient_id, format=None):
        pizza = Pizza.objects.get(id=pizza_id)
        ingredient = Ingredient.objects.get(id=ingredient_id)
        pizza.ingredients.remove(ingredient)
        return Response({
          "message": f"Se ha removido el ingrediente {ingredient} de la pizza {pizza}"
        })


############################# Endpoints of Ingredients #############################


class IngredientsAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)
      
    def post(self, request, format=None):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
      
class IngredientDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    @resource_checker(Ingredient)
    def get(self, request, pk, format=None):
        ingredient = Ingredient.objects.get(pk=pk)
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)

    @resource_checker(Ingredient)
    def put(self, request, pk, format=None):
        ingredient = Ingredient.objects.filter(id=pk).first()
        serializer = IngredientSerializer(ingredient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
    @resource_checker(Ingredient)
    def delete(self, request, pk, format=None):
        ingredient = Ingredient.objects.filter(id=pk).first()
        pizza_with_that_ingredient = Pizza.objects.filter(ingredients=ingredient).exists()
        # Si existe una pizza asociada con ese ingrediente no se podrá eliminar la misma.
        if pizza_with_that_ingredient:
            return Response({"message": "There is a pizza with that ingredient, it cannot be deleted"})
        else:
            ingredient.delete()
            return Response({"message": f"Ingredient '{ingredient}' deleted succesfully"}, status=status.HTTP_204_NO_CONTENT)


############################# Endpoints of Categories #############################


class CategoriesAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
      
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
      
class CategoryDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    @resource_checker(Category)
    def get(self, request, pk, format=None):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    @resource_checker(Category)
    def put(self, request, pk, format=None):
        category = Category.objects.filter(id=pk).first()
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
    @resource_checker(Category)
    def delete(self, request, pk, format=None):
        category = Category.objects.filter(id=pk).first()
        category.delete()
        return Response({"message": f"Category '{category}' deleted succesfully"}, status=status.HTTP_204_NO_CONTENT)
