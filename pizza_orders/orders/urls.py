from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),  # Pass the view function without parentheses
    path('login/', customer_login, name='customer_login'),
    path('register/', customer_register, name='customer_register'),
]