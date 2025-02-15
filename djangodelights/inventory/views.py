from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Ingredient, MenuItem, Purchase

def home(request):
    # Profit and revenue view
    return render(request, "inventory/home.html")

class IngredientList(ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"

class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete_form.html"
    
class MenuItemList(ListView):
    model = MenuItem
    template_name = "inventory/menu_item_list.html"

class PurchaseList(ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"
