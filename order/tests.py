from django.test import TestCase, Client

from .models import pizza, subs_platters, toppings, pasta_salads, order_list
from django.contrib.auth.models import User

# Create your tests here.

class orderTestCase(TestCase):

    def setup(self):
        user = User.objects.create_user(username="test1", password="test258")
        p = pizza.objects.get(type ="regular Pizza",large = 21.95)
        dp = subs_platters.objects.get(type="Dinner platters", dish_name="Gareden Salad")
        sb = subs_platters.objects.get(type="Subs", dish_name="Chicken Parmigana")
        tp = toppings.objects.get(topp_type="chesee")
        ps = pasta_salads.objects.get(name="pasta", plate_name="Baked Ziti w/Meatballs")
        sl = pasta_salads.objects.get(name="salads", plate_name="Greek Salad")
        total_price = p.large + dp.large + sb.large + ps.price + sl.price

        order_list.objects.create(user=user,pizza_ord=p,pizza_size="Large", dinner_platters=dp, platter_size ="Large", subs = sb, sub_size="Large", pasta=ps, salads=sl, pizza_topping=tp, total_price = total_price)

    def test_index(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
