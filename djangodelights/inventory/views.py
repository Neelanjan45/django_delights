from django.shortcuts import render
from django.views.generic import ListView

from .models import Ingredient, MenuItem, Purchase

class IngredientList(ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"
    
class MenuItemList(ListView):
    model = MenuItem
    template_name = "inventory/menu_item_list.html"

class PurchaseList(ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"
