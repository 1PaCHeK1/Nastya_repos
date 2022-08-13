from django.shortcuts import render

from app.utils import header_context
from .models import Product, ProductAmounts


def products(request):
    if hasattr(request, 'GET'):
        type = request.GET.get('type')
    
    if type:
        """ SELECT * FROM Product WHERE type.type = {type} """
        try: data = Product.objects.filter(type__type=type)
        except:
            data = Product.objects.all()
    else:
        """ SELECT * FROM Product """
        data = Product.objects.all()

    context = header_context(request)
    context.update({
        'title': 'Список продуктов',
        'products': data
    })
    
    return render(request, 'petstore/list_product.html', context)


def product(request, id):
    data = Product.objects.get(id=id)
    amount = ProductAmounts.objects.get(product__id=id)
    
    context = header_context(request)
    context.update({
        'title': 'Информация о продукте',
        'product': data,
        'amount': amount,
    })
    
    return render(request, 'petstore/product.html', context)

