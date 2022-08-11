from django.contrib import admin
from .models import (
    Product,
    ProductAmounts,
    ProductType
)
# Register your models here.
@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    display_list = "__all__"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    display_list = "__all__"

@admin.register(ProductAmounts)
class ProductAmountsAdmin(admin.ModelAdmin):
    display_list = "__all__"