from core.models import PizzaAbstract
from django.db import models


class Category(PizzaAbstract):
    """Category model of an ingredient"""


class Ingredient(PizzaAbstract):
    """Ingredient Model"""
    category = models.ManyToManyField('Category')


class Pizza(PizzaAbstract):
    """Pizza Model"""
    price = models.IntegerField()
    ingredients = models.ManyToManyField('Ingredient')
    is_active = models.BooleanField(default=True)
