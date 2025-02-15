from django.db import models

class Ingredient(models.Model):
    ing_name = models.CharField(max_length=50)
    ing_quantity = models.FloatField(default=0.0)
    ing_unit = models.CharField(max_length=10, null=True)
    ing_unit_price = models.FloatField(default=0.0)

    def __str__(self):
        return self.ing_name

class MenuItem(models.Model):
    menu_name = models.CharField(max_length=100)
    menu_price = models.FloatField(default=0.0)

    def __str__(self):
        return f"{ self.menu_name } - { str(self.menu_price) }"

class RecipeRequirement(models.Model):
    rec_menu = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    rec_ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    rec_ing_quantity = models.FloatField(default=0.0)

    def __str__(self):
        return f"{ self.rec_menu.menu_name }, { self.rec_ingredient.ing_name } - { str(self.rec_ing_quantity) }"

class Purchase(models.Model):
    pur_menu = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    pur_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{ str(self.pur_date.strftime('%b %d, %Y')) } - { self.pur_menu.menu_name } - { str(self.pur_menu.menu_price) }"
