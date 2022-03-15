from django.contrib import admin
from product.models import Pizza, Ingredient, Category

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active',)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

        
admin.site.register(Pizza ,PizzaAdmin)
admin.site.register(Ingredient ,IngredientAdmin)
admin.site.register(Category ,CategoryAdmin)