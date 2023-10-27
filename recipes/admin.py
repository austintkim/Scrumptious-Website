from django.contrib import admin
from recipes.models import Recipe, RecipeStep, RecipeIngredient

# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "id",
        "description",
        "created_on",
        "updated_on"
    ]

@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = [
        "step_number",
        "instruction",
        "id",
    ]

@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = [
        "amount",
        "food_item",
        "recipe",
    ]
