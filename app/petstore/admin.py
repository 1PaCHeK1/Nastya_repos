from django.contrib import admin
from .models import (
    Product,
    ProductAmounts,
    ProductType,
    Order
)

# Register your models here.
@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    display_list = "__all__"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    display_list = ('id', 'name')

@admin.register(ProductAmounts)
class ProductAmountsAdmin(admin.ModelAdmin):
    display_list = "__all__"

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    display_list = "__all__"