from django.db import models
from core.models import PizzaAbstract


class Category(PizzaAbstract):
    """Category model of an ingredient. """


class Ingredient(PizzaAbstract):
    """Ingredient Model. """
    category = models.ManyToManyField('Category')
    

class Pizza(PizzaAbstract):
    """Pizza Model. """
    price = models.IntegerField('Precio')
    ingredients = models.ManyToManyField('Ingredient', null=False)
    is_active = models.BooleanField(default=True)
    