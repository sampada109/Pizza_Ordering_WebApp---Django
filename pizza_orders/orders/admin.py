from django.contrib import admin
from .models import *

# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available')

admin.site.register(Size)
admin.site.register(Topping)
admin.site.register(Pizza,PizzaAdmin)
admin.site.register(CustomerOrder)
admin.site.register(OrderItem)