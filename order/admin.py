from django.contrib import admin

from .models import pizza, toppings, subs_platters, pasta_salads, order_list

# Register your models here.


admin.site.register(pizza)
admin.site.register(toppings)
admin.site.register(subs_platters)
admin.site.register(pasta_salads)
admin.site.register(order_list)
