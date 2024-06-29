from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.


def index(request):
    menu = Pizza.objects.all()
    return render(request, 'index.html', {'menu':menu})


#login
def customer_login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user_obj = User.objects.filter(username = username)

            if not user_obj.exists():
                messages.error(request, 'user not found!')
                return redirect('customer_register')

            user_obj = authenticate(username = username, password = password)

            if user_obj:
                login(request, user_obj)
                return redirect('/')
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('customer_login')
            
        except Exception as e:
            messages.error(request, e)
            return redirect('customer_login')
        
    return render(request, 'login.html')


#register
def customer_register(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            user_obj = User.objects.filter(username = username)

            if user_obj.exists():
                messages.error(request, 'username already exists!')
                return redirect('customer_register')
            
            user_obj = User.objects.create(username = username, email = email)
            user_obj.set_password(password)
            user_obj.save()

            messages.success(request, 'user successfully created!')

            return redirect('/')
        except Exception as e:
            messages.error(request, e)
            return redirect('customer_register')
        
    return render(request, 'register.html')


#logout
def user_logout(request):
    logout(request)
    return redirect('/')


#user profile - account page
def user_account(request):
    return render(request, 'account.html')


#pizza detailed page
def pizza_detail(request, pz_id):
    pizza = Pizza.objects.get(uid = pz_id)
    veg_topping = Topping.objects.filter(category='Veg')
    non_veg_topping = Topping.objects.filter(category='Non-Veg')
    return render(request, 'pizza_detail.html', {'pizza':pizza, 'veg_topping':veg_topping, 'non_veg_topping':non_veg_topping})