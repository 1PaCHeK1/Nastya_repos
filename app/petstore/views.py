from django.shortcuts import render
from .models import Product


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
    
    context = {
        'title': 'Список продуктов',
        'products': data
    }
    
    return render(request, 'petstore/list_product.html', context)