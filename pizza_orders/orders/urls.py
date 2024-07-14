from django.urls import path
from .views import *

urlpatterns = [
    path('menu/', index, name='index'),  # Pass the view function without parentheses
    path('login/', customer_login, name='customer_login'),
    path('register/', customer_register, name='customer_register'),
    path('logout/', user_logout, name='user_logout'),
    path('account/', user_account, name='user_account'),
    path('pizza_detail/<uuid:pz_id>/', pizza_detail, name='pizza_detail'),
    path('add_item_cart/<uuid:pz_id>/', add_item_cart, name='add_item_cart'),
    path('cart_view/', cart_view, name='cart_view'),
    path('customize_cart/<uuid:order_item_id>', customize_cart, name='customize_cart'),
    path('delete_cart_item/<uuid:order_item_id>', delete_cart_item, name='delete_cart_item'),
    path('order_payment/', order_payment, name='order_payment'),
    path('payment_success/', payment_success, name='payment_success'),
    path('', home, name='home'),
]