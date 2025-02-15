from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement

class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["ing_name", "ing_quantity", "ing_unit", "ing_unit_price"]
        labels = {
            "ing_name": "Ingredient Name",
            "ing_quantity": "Quantity",
            "ing_unit": "Unit",
            "ing_unit_price": "Price per Unit",
        }

class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ["menu_name", "menu_price"]
        labels = {
            "menu_name": "Menu Name",
            "menu_price": "Price",
        }

class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ["rec_menu", "rec_ingredient", "rec_ing_quantity"]
        labels = {
            "rec_menu": "Select Menu",
            "rec_ingredient": "Select Ingredient",
            "rec_ing_quantity": "Quantity"
        }
