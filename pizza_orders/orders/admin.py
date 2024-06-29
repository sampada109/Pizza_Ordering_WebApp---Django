from django.contrib import admin
from .models import *

# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available')

class SizeAdmin(admin.ModelAdmin):
    list_display = ('size', 'price')

class ToppingAdmin(admin.ModelAdmin):
    list_display = ('topping_name', 'category', 'price')

admin.site.register(Size, SizeAdmin)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(Pizza,PizzaAdmin)
admin.site.register(CustomerOrder)
admin.site.register(OrderItem)