from django.contrib import admin

from django.contrib import admin
from .models import Order, Product, OrderItem ,User # Import your models

# Register your models
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(OrderItem)
