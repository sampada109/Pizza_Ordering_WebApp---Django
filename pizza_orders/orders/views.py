from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    menu = Pizza.objects.all()
    return render(request, 'index.html', {'menu':menu})