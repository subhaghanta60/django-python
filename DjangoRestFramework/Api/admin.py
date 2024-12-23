from django.contrib import admin

from django.contrib import admin
from .models import Order, Product, OrderItem ,User # Import your models

from Api.models import Order,OrderItem

class OrderItemInline(admin.TabularInline):
    model=OrderItem


class OrderAdmin(admin.ModelAdmin):
        inlines = [
            OrderItemInline
        ]
    

admin.site.register(Order, OrderAdmin)
# Register your models
admin.site.register(User)

admin.site.register(Product)
admin.site.register(OrderItem)



# User pythondev
# password python12345