from django.contrib import admin
from .models import *


# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display= ["name", "price", "post_date", "brand"]
    search_fields = ["name", "post_date"]
    list_filter = ["price", "post_date"]
admin.site.register(Products, ProductsAdmin)

admin.site.register(Category)
admin.site.register(OrderItem)
admin.site.register(Order)
