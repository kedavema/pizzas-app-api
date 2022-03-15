from django.urls import path
from product.views import (
                            PizzasAPIView, PizzaDetailAPIView,
                            IngredientsAPIView, IngredientDetailAPIView,
                            CategoriesAPIView, CategoryDetailAPIView,
                           )


app_name = 'product'


urlpatterns = [
    path('pizzas', PizzasAPIView.as_view(), name='pizzas'),
    path('pizzas/<int:pk>', PizzaDetailAPIView.as_view(), name='pizza-detail'),
    path('ingredients', IngredientsAPIView.as_view(), name='ingredients'),
    path('ingredients/<int:pk>', IngredientDetailAPIView.as_view(), name='ingredient-detail'),
    path('categories', CategoriesAPIView.as_view(), name='categories'),
    path('categories/<int:pk>', CategoryDetailAPIView.as_view(), name='category-detail'),
]