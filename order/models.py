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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_users")
    total_price = models.FloatField()
    
