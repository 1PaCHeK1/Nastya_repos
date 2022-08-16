from django.dispatch import receiver
from django.db.models.signals import (
    pre_save, 
    post_save,
    pre_delete,
    post_delete
)

from .models import (
    Product,
    ProductAmounts
)


@receiver(post_save, sender=Product)
def create_product_amount(sender, instance:Product, *args, **kwargs):
    pa = ProductAmounts.objects.filter(product__id=instance.id)
    if not pa:
        ProductAmounts.objects.create(
            product=instance,
            amount =10    
        )
