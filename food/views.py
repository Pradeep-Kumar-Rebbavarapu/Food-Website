from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import *
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.views.generic.detail import *
from django.views.generic.list import *
from django.db.models import Count
from django.contrib.auth.models import Permission
# Create your views here.
def home(request):
    print(' I am View')
    nav= {
        ''
    }
    params = {
        'nav':nav,
    }
    return render(request,'home/home.html',params)

def Signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            
            # username = fm.cleaned_data['username']
            # password1 = fm.cleaned_data['password1']
            # email = fm.cleaned_data['email']
            # first_name = fm.cleaned_data['first_name']
            # last_name = fm.cleaned_data['last_name']
            # user = User.objects.create(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
            # user.save()
            messages.add_message(request,messages.SUCCESS,'Your Account Has Been Created')
    else:
        fm = SignupForm()
    params = {
        'fm':fm
    }
    return render(request,'auth/Signup.html',params)
def Login(request):
    if request.method == 'POST':
        fm = LoginForm(request=request,data=request.POST)
        if fm.is_valid():
            print(fm)
            username = fm.cleaned_data['username']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            user = authenticate(username=username,password=password)
            
            if email!=user.email:
                messages.add_message(request,messages.ERROR,'User Not Found')
            else:
                if user is not None:
                    login(request,user)
                    messages.add_message(request,messages.SUCCESS,'You Have Logged In Succesfully')
                    return HttpResponseRedirect('/')
    else:
        fm = LoginForm()
    params = {
        'fm':fm
    }
    return render(request,'auth/Login.html',params)
def Order(request):
    queryset = item.objects.all()
    # print(queryset)
    params = {
        'items1':queryset[:6],
        'items2':queryset[6:]
    }
    return render(request,'food/Order.html',params)

def Logout(request):
    user=request.user
    print(user)
    print(user.is_authenticated)
    logout(request)
    return HttpResponseRedirect('/Login')

def EachItem(request,pk):
    queryset = item.objects.filter(item_id=pk)
    params = {
        "eachitem":queryset
    }
    return render(request,'food/EachItem.html',params)

def YourCart(request):
    if request.method=='POST':
        id = request.POST['id']
        user1 = request.POST['user']
        user = request.user
        print(user1)                                     
        fooditem = item.objects.get(item_id=id)
        usercart = Cart.objects.filter(user=user).filter(fooditem=fooditem)
        if usercart.exists():
            print('exists')
            for i in usercart:
                print('inside for loop')
                print(i)
                i.quantity=i.quantity+1
                i.TotalPrice = fooditem.price*i.quantity
                i.save()   
        else:
            print('no000000000000000')
            cart = Cart(user=user,fooditem=fooditem,quantity=1,TotalPrice=(fooditem.price))
            cart.save()
        print('fooditem',fooditem)
        print('usercart',usercart)
        return HttpResponseRedirect(f'/EachItem/{id}')
    user=request.user
    queryset = Cart.objects.filter(user=user)
    print('get',queryset)
    params = {
        'displaycart':queryset
    }
    return render(request,'food/Cart.html',params)

# Gangsta@11519