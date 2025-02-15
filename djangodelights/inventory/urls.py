from django.urls import path
from . import views

urlpatterns = [
    path("ingredient/list", views.IngredientList.as_view(), name="ingredients"),
    path("menu/list", views.MenuItemList.as_view(), name="menuitems"),
    path("purchase/list", views.PurchaseList.as_view(), name="purchases"),
]
