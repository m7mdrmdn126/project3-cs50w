from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class pizza(models.Model):
    pizzas_type = [
        ('sicilian Pizza', 'Sicilian Pizza'),
        ('regular Pizza', 'Regular Pizza')
    ]
    toppings_list = [
        ('chesee', 'chesee'),
        ('1 toppings','1 toppings' ),
        ('2 toppings','2 toppings' ),
        ('3 toppings','3 toppings' )
    ]
    topp = models.CharField(max_length=64, choices=toppings_list, default='chesee')
    type = models.CharField(max_length=64, choices=pizzas_type, default="regular Pizza")
    large = models.FloatField()
    small = models.FloatField()

    def __str__(self):
        return f"{self.type}, {self.topp} price : {self.large} for Large, {self.small} for small ."

class subs_platters(models.Model):
    kind = [
        ('platters', 'Dinner Platters'),
        ('sub','sub')
    ]
    type = models.CharField(max_length=64, choices=kind, default="platters")
    dish_name = models.CharField(max_length=64)
    large = models.FloatField()
    small = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.type} , {self.dish_name} large for {self.large}, small for {self.small}"


class toppings(models.Model):
    topp_type = models.CharField(max_length=64)

    def __str__(self):
        return f" Topping {self.topp_type}"


class pasta_salads(models.Model):
    kind = [
        ('pasta', 'pasta'),
        ('salads', 'salads')
    ]
    name = models.CharField(max_length=64, choices=kind)
    plate_name = models.CharField(max_length=64, blank=True)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}: {self.plate_name}, for : {self.price}"



class order_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_users", blank=True, null=True)
    pizza_ord = models.ForeignKey(pizza, on_delete=models.CASCADE, related_name="pizza_order", blank=True, null=True)
    pizza_size = models.CharField(max_length=64, blank=True, null=True)
    dinner_platters = models.ForeignKey(subs_platters, on_delete=models.CASCADE, related_name="platters", blank=True, null=True)
    platter_size = models.CharField(max_length=64, blank=True, null=True)
    subs = models.ForeignKey(subs_platters, on_delete=models.CASCADE, related_name="subs", blank=True, null=True)
    sub_size = models.CharField(max_length=64, blank=True, null=True)
    pasta = models.ForeignKey(pasta_salads, on_delete=models.CASCADE, related_name="pasta", blank=True, null=True)
    salads = models.ForeignKey(pasta_salads, on_delete=models.CASCADE, related_name="salads", blank=True, null=True)
    total_price = models.FloatField()
    pizza_topping = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        if self.pizza_ord == None:
            pizza_syn = "No pizza ordered"
        else:
            pizza_syn = f" {self.pizza_size},{self.pizza_ord.type} with {self.pizza_ord.topp} "

        if self.dinner_platters == None:
            platter_syn = "No platters ordered"
        else:
            platter_syn = f" {self.platter_size},{self.dinner_platters.dish_name} "

        if self.subs == None:
            subs_syn = "No subs ordered"
        else:
            subs_syn = f" {self.sub_size},{self.subs.dish_name} "


        if self.pasta == None:
            pasta_syn = "No pasta ordered"
        else:
            pasta_syn = f" {self.pasta.plate_name} "

        if self.salads == None:
            salads_syn = "No salads ordered"
        else:
            salads_syn = f" {self.salads.plate_name} "

        return f"{self.user.username} ordered: {pizza_syn}, {platter_syn}, {subs_syn}, {pasta_syn}, {salads_syn}"
