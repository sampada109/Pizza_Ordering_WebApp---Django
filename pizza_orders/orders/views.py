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
    size = Size.objects.all()
    veg_topping = Topping.objects.filter(category='Veg')
    non_veg_topping = Topping.objects.filter(category='Non-Veg')

    # print(pizza.name)
    return render(request, 'pizza_detail.html', {'pizza':pizza, 'veg_topping':veg_topping, 'non_veg_topping':non_veg_topping, 'size':size})


# add pizza to cart 
def add_item_cart(request, pz_id):
    pizza = Pizza.objects.get(uid = pz_id)

    # pizza detail page 
    if request.method == 'POST':
        size_name = request.POST.get('size')
        quantity = int(request.POST.get('quantity'))
        toppings_list = request.POST.getlist('toppings')

        print("*** ",pizza.name, size_name, quantity, toppings_list)

        size = Size.objects.get(size=size_name)
        toppings = Topping.objects.filter(topping_name__in=toppings_list)

        # calculate price
        # total_price = pizza.price + size.price
        # for top in toppings:
        #     total_price += top.price
        # total_price *= quantity

        total_price = OrderItem.total_price()

        #create or get the order
        order, created = CustomerOrder.objects.get_or_create(user = request.user)

        # create OrderItem 
        order_item = OrderItem.objects.create(
            order = order,
            pizza = pizza,
            size = size,
            quantity = quantity,
            price = total_price
        )

        order_item.topping.set(toppings)
        order_item.save()

        return redirect('/')

    #pizza through index page
    else:
        size = Size.objects.all()[:1].get()
        quantity = 1
        toppings = Topping.objects.none()  #no default toppings

        total_price = OrderItem.total_price()

        #create or get the order
        order, created = CustomerOrder.objects.get_or_create(user = request.user)

        # create OrderItem 
        order_item = OrderItem.objects.create(
            order = order,
            pizza = pizza,
            size = size,
            quantity = quantity,
            price = total_price
        )

        order_item.topping.set(toppings)
        order_item.save()
        
        return redirect('/')
    

# cart page 
def cart_view(request):
    #get current user pending orders 
    customer_orders = CustomerOrder.objects.get(user = request.user, status = 'Pending')

    #check if there is any pending order or not
    if not customer_orders:
        items = []
        order_total = 0
    else:
        items = OrderItem.objects.filter(order = customer_orders)
        # calculate total price for the order 
        order_total = sum(item.price for item in items)

        customer_orders.total_amount = order_total
        customer_orders.save()

    return render(request, 'cart.html', {'items':items, 'order_total':order_total})


# customise cart item 
# def customize_cart(request, order_item_id):
#     order_item = OrderItem.objects.get(uid = order_item_id)
#     pizza = order_item.pizza

#     # if any update id done 
#     if request.method == 'POST':
#         size = request.POST.get('size')
#         quantity = int(request.POST.get('quantity'))
#         topping_list = request.POST.getlist('toppings')

#         #update existing order items
#         order_item.size = Size.objects.get(size=size)
#         order_item.quantity = quantity
#         toppings = Topping.objects.filter(topping_name__in = topping_list)
#         order_item.topping.set(toppings)
#         total_price = pizza.price + size.price
#         for top in toppings:
#             total_price += top.price
#         total_price *= quantity
#         order_item.price = total_price

#         order_item.save()

#         return redirect('cart_view')
    
#     else:
#         size = order_item.size
#         quantity = order_item.quantity
#         veg_toppings = Topping.objects.filter(category='Veg') 
#         non_veg_toppings = Topping.objects.filter(category='Non-Veg') 

#     return render(request, 'pizza_detail.html', {'pizza':pizza, 'selected_order_item':order_item,'selected_size':size, 'veg_topping':veg_toppings, 'non_veg_topping':non_veg_toppings})


# deleting item from cart
def delete_cart_item(request, order_item_id):
    try:
        OrderItem.objects.get(uid = order_item_id).delete()
        return redirect('cart_view')
    except Exception as e:
        return redirect('cart_view', e)