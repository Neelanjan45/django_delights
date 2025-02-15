from django.db import models

class Ingredient(models.Model):
    ing_name = models.CharField(max_length=50)
    ing_quantity = models.FloatField(default=0.0)
    ing_unit = models.CharField(max_length=10, null=True)
    ing_unit_price = models.FloatField(default=0.0)

class MenuItem(models.Model):
    menu_name = models.CharField(max_length=100)
    menu_price = models.FloatField(default=0.0)

class RecipeRequirement(models.Model):
    rec_menu = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    rec_ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    rec_ing_quantity = models.FloatField(default=0.0)

class Purchase(models.Model):
    pur_menu = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    pur_date = models.DateTimeField(auto_now_add=True)
