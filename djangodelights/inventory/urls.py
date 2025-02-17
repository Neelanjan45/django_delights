from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("account/", include("django.contrib.auth.urls"), name="login"),

    path("ingredient/list", views.IngredientList.as_view(), name="ingredients"),
    path("ingredient/create", views.IngredientCreate.as_view(), name="ingredientcreate"),
    path("ingredient/update/<pk>", views.IngredientUpdate.as_view(), name="ingredientupdate"),
    path("ingredient/delete/<pk>", views.IngredientDelete.as_view(), name="ingredientdelete"),
    path("menu/list", views.MenuItemList.as_view(), name="menuitems"),
    path("menu/create", views.MenuItemCreate.as_view(), name="menuitemcreate"),
    path("purchase/list", views.PurchaseList.as_view(), name="purchases"),
    path("recipe/create", views.RecipeRequirementCreate.as_view(), name="reciperequirement"),

    path("logout/", views.logout_view, name="logout")
]
