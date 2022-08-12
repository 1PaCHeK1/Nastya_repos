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
    amounts = [amount[2] for amount in ProductAmounts.objects.filter(product=id).values_list()]
    
    context = header_context(request)
    context.update({
        'title': 'Список продуктов',
        'product': data,
        'amounts': amounts,
    })
    
    return render(request, 'petstore/product.html', context)

