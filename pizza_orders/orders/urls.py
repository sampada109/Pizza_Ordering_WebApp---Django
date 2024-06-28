from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),  # Pass the view function without parentheses
]