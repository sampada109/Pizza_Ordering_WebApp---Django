from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid


# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


# class PizzaCategory(BaseModel):
#     category_name = models.CharField(max_length=100)


class Size(BaseModel):
    size = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Topping(models.Model):
    CATEGORY_CHOICE = [
        ('Veg', 'Veg'), ('Non-Veg', 'Non-Veg')
    ]
    topping_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICE, null=True)


class Pizza(BaseModel):
    CATEGORY_CHOICE = [
        ('Veg', 'Veg'), ('Non-Veg', 'Non-Veg')
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    pizza_image = models.ImageField(upload_to="pizza_image/", null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)



class CustomerOrder(BaseModel):
    STATUS_CHOICES = [
        ('Pending', 'Pending'), ('Completed', 'Completed')
    ]
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')


class OrderItem(BaseModel):
    order = models.ForeignKey(CustomerOrder, related_name='items', on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    topping = models.ManyToManyField(Topping, blank=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)