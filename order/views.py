from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from .models import pizza, toppings, subs_platters, pasta_salads, order_list

import json

# Create your views here.
message = ''

def index(request):
    # checking if the user is authintcated and if not make him back to the login menu 
    if not request.user.is_authenticated :
        return render(request, 'order/login.html')
        

    # getting the data frrom the data base and send
    try:
        user = order_list.objects.get(user = request.user)
    except :
        user = ''

    print(user)

    context = {
        "regular_pizza":pizza.objects.filter(type='regular Pizza'),
        "sicilian_pizza":pizza.objects.filter(type='sicilian Pizza'),
        "toppings":list(toppings.objects.all()),
        "subs":subs_platters.objects.filter(type="Subs"),
        "platters":subs_platters.objects.filter(type="Dinner platters"),
        "pasta":pasta_salads.objects.filter(name="pasta"),
        "salads":pasta_salads.objects.filter(name="salads"),
        "message":message,
        "order":user,
        "username":request.user,
    }
    print(message)
    return render(request, "order/index.html", context)


def order(request):
    global message
    # this the function responsable to add the orders to the data base 

    # making an order list object 
    user_ord = request.user

    # setting the price 
    total_pricee = 0

    # adding the user to the order list 
    order_com = order_list(user = user_ord)

    # requesting pizza from the client side 
    pizza_t = request.GET["pizza_type"]
    print(pizza_t)
    """ ok all of thoso things are going in a regular system as they request the information 
     from the clent side then adding them to the backend and adding them to the database 
     to make them recalable and easy to the owner of the resturant to know the order"""
    if pizza_t != "None" :
        pizza_topp = request.GET["pizza_topp"]
        pizza_size = request.GET["pizza_size"]
        pizza_ex = True
        if pizza_topp != "None" and pizza_topp != "chesee":
            topp = request.GET["topping"]
            if topp == "None":
                message = "please select topping for pizza."
                return HttpResponseRedirect(reverse("index"))
            else :
                order_com.pizza_topping = topp 
        elif pizza_topp == "None":
            message = "please select topping number for pizza."
            print(message)
            return HttpResponseRedirect(reverse("index"))
        elif pizza_size == "None":
            message = "please select size for pizza."
            return HttpResponseRedirect(reverse("index"))
        

    else:
        pizza_ex = False 
    
    if pizza_ex == True:
        p_order = pizza.objects.get(type=pizza_t, topp=pizza_topp)
        order_com.pizza_ord = p_order
        if pizza_size == "large": 
            total_pricee += p_order.large
            order_com.pizza_size = "Large"
        elif pizza_size == "small":
            total_pricee += p_order.small
            order_com.pizza_size = "Small"

    
    """ the algorithm is somthing we can say it's smillar as we are after getting the data from 
    the client side then we checking if the user made all things in the right way and 
    raising errors with if condetions if the platte or any thing else is callen by the 
    user we make it exist just with a boolean var."""

    # requesting platters from the client side 
    platter_name = request.GET["dinner_platters"]
    print(platter_name)
    if platter_name != "None" :
        platters_ex = True
        platter_size = request.GET["plate_size"]
        if platter_size == "None":
            message = "please enter the dinner platter Size"
            return  HttpResponseRedirect(reverse("index"))

    else:
        platters_ex = False 
    
    if platters_ex == True :
        platter_ord = subs_platters.objects.get(type="Dinner platters", dish_name=platter_name)
        order_com.dinner_platters = platter_ord 
        if platter_size == "large": 
            total_pricee += platter_ord.large
            order_com.platter_size = "Large"
        elif platter_size == "small":
            order_com.platter_size = "Small"
            total_pricee += platter_ord.small
       

     # requesting subs from the client side 
    sub_name = request.GET["subs"]
    if sub_name != "None" :
        subs_ex = True
        sub_size = request.GET["sub_size"]
        if sub_size == "None":
            message = "please enter the sub Size"
            return  HttpResponseRedirect(reverse("index"))

    else:
        subs_ex = False 
    
    if subs_ex == True:
        sub_ord = subs_platters.objects.get(type="Subs", dish_name=sub_name)
        order_com.subs = sub_ord
        if sub_size == "large":
            order_com.sub_size = "Large" 
            total_pricee += sub_ord.large
        elif sub_size == "small":
            order_com.sub_size = "Small"
            total_pricee += sub_ord.small
        

    
      # requesting pasta from the client side 
    pasta_dish = request.GET["pasta"]
    if pasta_dish != "None" :
        pasta_ex = True
    else:
        pasta_ex = False 
    
    if pasta_ex  == True:
        pasta_ord = pasta_salads.objects.get(name="pasta", plate_name=pasta_dish)
        order_com.pasta = pasta_ord
        total_pricee += pasta_ord.price
    
       # requesting salads from the client side 
    salad_dish = request.GET["salads"]
    if salad_dish != "None" :
        salad_ex = True
    else:
        salad_ex = False 
    
    if salad_ex == True:
        salad_ord = pasta_salads.objects.get(name="salads", plate_name=salad_dish)
        order_com.salads = salad_ord
        total_pricee += salad_ord.price


    order_com.total_price = total_pricee

    order_com.save()
    return  HttpResponseRedirect(reverse("index"))





def toppin(request):
    """ this function return the topping list to the client side with ajax response """

    toppings_name = toppings.objects.all()
    top = []
    for topp in toppings_name:
        top.append(topp.topp_type)

    return JsonResponse(list(top), safe=False)
    



def login_view(request):
    """ login to an alredy exisited user """

    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    context = {
        'message':"invalid cardintials ."
    }
    return render(request, "order/login.html", context)



def register(request):
    """ create a user and add it to the database. """

    reg_username = request.POST["reg-username"]
    reg_mail = request.POST["reg-Email"]
    reg_password = request.POST["reg-password"]


    try:
        user = User.objects.create_user(username=reg_username, email=reg_mail, password=reg_password)
    except:
        return render(request, "order/login.html", {'message':"This username is not avilable ."})


    user.save()
    return render(request, "order/login.html", {'message':"Done sucssufuly ."})



def logout_view(request):
    logout(request)
    return render(request, "order/login.html")
