from django.contrib import admin
from .models import (
    Product,
    ProductAmounts
)
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    display_list = "__all__"

@admin.register(ProductAmounts)
class ProductAmountsAdmin(admin.ModelAdmin):
    display_list = "__all__"
