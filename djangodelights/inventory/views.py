from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Ingredient, MenuItem, Purchase
from .forms import IngredientCreateForm, MenuItemCreateForm

def home(request):
    # Profit and revenue view
    return render(request, "inventory/home.html")

class IngredientList(ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"

class IngredientCreate(CreateView):
    model = Ingredient
    template_name = "inventory/ingredient_create_form.html"
    form_class = IngredientCreateForm

class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete_form.html"
    
class MenuItemList(ListView):
    model = MenuItem
    template_name = "inventory/menu_item_list.html"

class MenuItemCreate(CreateView):
    model = MenuItem
    template_name = "inventory/menu_item_create_form.html"
    form_class = MenuItemCreateForm

class PurchaseList(ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"
