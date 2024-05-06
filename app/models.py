from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    _status = (
        ('Pending', 'Pending'), 
        ('Accepted', 'Accepted')
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=_status, default='Pending')

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)


# ================
