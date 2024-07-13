from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from instamojo_wrapper import Instamojo
from django.conf import settings
from django.urls import reverse


api = Instamojo(api_key=settings.INSTAMOJO_API_KEY,
                auth_token=settings.INSTAMOJO_AUTH_TOKEN,
                endpoint=settings.INSTAMOJO_ENDPOINT)



# Create your views here.


def index(request):
    menu = Pizza.objects.all().order_by('-updated_at')
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
    user = User.objects.get(username = request.user.username)
    customer_order = CustomerOrder.objects.filter(user = request.user).order_by('-updated_at')
    return render(request, 'account.html', {'user':user, 'customer_order':customer_order})


#pizza detailed page
def pizza_detail(request, pz_id, item_id=None):
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
        total_price = pizza.price + size.price
        for top in toppings:
            total_price += top.price
        total_price *= quantity

        #create or get the order
        order, created = CustomerOrder.objects.get_or_create(user = request.user, status='Pending')

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

        # calculate price 
        total_price = pizza.price + size.price

        #create or get the order
        order, created = CustomerOrder.objects.get_or_create(user = request.user, status='Pending')

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
    customer_orders = CustomerOrder.objects.filter(user = request.user, status = 'Pending').first()
    order_count = OrderItem.objects.filter(order=customer_orders).count()

    #to display in the cutomised order
    select_size = Size.objects.all()
    select_veg_top = Topping.objects.filter(category='Veg')
    select_non_top = Topping.objects.filter(category='Non-Veg')

    
    #check if there is any pending order or not
    if customer_orders:
        items = OrderItem.objects.filter(order = customer_orders).order_by('-created_at')
        # calculate total price for the order 
        order_total = sum(item.price for item in items)

        customer_orders.total_amount = order_total
        customer_orders.item_in_cart = order_count
        customer_orders.save()



    else:
        items = []
        order_total = 0

    return render(request, 'cart.html', {'items':items, 'order_total':order_total, 'select_size':select_size, 'select_veg_top':select_veg_top, 'select_non_top':select_non_top})


# customise cart item 
def customize_cart(request, order_item_id):
    order_item = OrderItem.objects.get(uid = order_item_id)
    pizza = order_item.pizza

    # if any update id done 
    if request.method == 'POST':
        size = request.POST.get('size')
        quantity = int(request.POST.get('quantity'))
        topping_list = request.POST.getlist('toppings')

        #update existing order items
        order_item.size = Size.objects.get(size=size)
        order_item.quantity = quantity
        toppings = Topping.objects.filter(topping_name__in = topping_list)
        order_item.topping.set(toppings)
        total_price = pizza.price + order_item.size.price
        for top in toppings:
            total_price += top.price
        total_price *= quantity
        order_item.price = total_price

        order_item.save()

        return redirect('cart_view')
    
    else:
        all_size = Size.objects.all()
        all_veg_top = Topping.objects.filter(category='Veg')
        all_non_top = Topping.objects.filter(category='Non-Veg')
        select_size = order_item.size
        select_quantity = order_item.quantity
        select_veg_top = order_item.topping.filter(category='Veg') 
        select_non_top = order_item.topping.filter(category='Non-Veg')
        print(order_item.size.size)
        print(order_item.quantity)
        print(order_item.topping.all().values())
        print(order_item.topping.filter(category='Veg').all().values())
        print(order_item.topping.filter(category='Non-Veg').all().values())
        print(pizza.name)

        context = {
            'all_size':all_size,
            'all_veg_top':all_veg_top,
            'all_non_top':all_non_top,
            'select_size':select_size,
            'select_quantity':select_quantity,
            'select_veg_top':select_veg_top,
            'select_non_top':select_non_top,
            'pizza':pizza
        }

    return render(request, 'customize_order.html', {'context':context})


# deleting item from cart
def delete_cart_item(request, order_item_id):
    try:
        OrderItem.objects.get(uid = order_item_id).delete()
        return redirect('cart_view')
    except Exception as e:
        return redirect('cart_view', e)



#order payment
def order_payment(request):
    #get current user pending orders 
    customer_orders = CustomerOrder.objects.get(user = request.user, status = 'Pending')
    order_count = OrderItem.objects.filter(order=customer_orders).count()
    
    response = api.payment_request_create(
        amount= str(customer_orders.total_amount),
        purpose= 'Order Payment',
        buyer_name= request.user.username,
        email= request.user.email,
        redirect_url= request.build_absolute_uri(reverse('payment_success')),
    )
    print(response)

    return redirect(response['payment_request']['longurl'])


#payment result
def payment_success(request):
    payment_request_id = request.GET.get('payment_request_id')
    payment_id = request.GET.get('payment_id')
    status = request.GET.get('payment_status')

    if status == 'Credit':
        customer_order = CustomerOrder.objects.get(user = request.user, status = 'Pending')
        if customer_order:
            customer_order.status = 'Completed'
            customer_order.save()
            return render(request, 'payment_result.html', {'status':'success'})
        
    return render(request, 'payment_result.html', {'status':'fail'})