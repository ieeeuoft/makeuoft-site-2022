from django.contrib import admin
from .models import Hardware, Category, Order, Incident, OrderItem

# Register your models here.
admin.site.register(Hardware)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Incident)
admin.site.register(OrderItem)
