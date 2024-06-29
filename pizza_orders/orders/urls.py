from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),  # Pass the view function without parentheses
    path('login/', customer_login, name='customer_login'),
    path('register/', customer_register, name='customer_register'),
    path('logout/', user_logout, name='user_logout'),
    path('account/', user_account, name='user_account'),
    path('pizza_detail/<uuid:pz_id>/', pizza_detail, name='pizza_detail'),
]