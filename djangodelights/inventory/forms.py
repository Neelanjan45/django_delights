from django import forms
from .models import Ingredient, MenuItem

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
