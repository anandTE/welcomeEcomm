from django.contrib import admin

# Register your models here.




from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer, Item, Order, OrderItem, Payment
from .forms import CustomerCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomerCreationForm

admin.site.register(Customer, CustomUserAdmin)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
