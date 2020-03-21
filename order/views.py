from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from .models import pizza, toppings, subs_platters, pasta_salads

# Create your views here.

def index(request):
    if not request.user.is_authenticated :
        return render(request, 'order/login.html')

    context = {
        "regular_pizza":pizza.objects.filter(type='regular Pizza'),
        "sicilian_pizza":pizza.objects.filter(type='sicilian Pizza'),
        "toppings":toppings.objects.all(),
        "subs":subs_platters.objects.filter(type="Subs"),
        "platters":subs_platters.objects.filter(type="Dinner platters"),
        "pasta":pasta_salads.objects.filter(name="pasta"),
        "salads":pasta_salads.objects.filter(name="salads"),
    }

    return render(request, "order/index.html", context)


def order(request):
    pass


def login_view(request):
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
