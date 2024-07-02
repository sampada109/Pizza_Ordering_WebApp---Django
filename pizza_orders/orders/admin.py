from django.contrib import admin
from .models import *

# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available')

class SizeAdmin(admin.ModelAdmin):
    list_display = ('size', 'slices', 'price')

class ToppingAdmin(admin.ModelAdmin):
    list_display = ('topping_name', 'category', 'price')

class CutomerOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_amount','status')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'price')

admin.site.register(Size, SizeAdmin)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(Pizza,PizzaAdmin)
admin.site.register(CustomerOrder, CutomerOrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)