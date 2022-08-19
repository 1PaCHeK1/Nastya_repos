from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from app.utils import header_context
from .models import Product, ProductAmounts, Order
from django.contrib.auth.decorators import login_required


class ProductsView(View):
    def get(self, request, *args, **kwargs):
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

class ProductView(View):
    def get(self, request, id, *args, **kwargs):
        data = Product.objects.get(id=id)
        amount = ProductAmounts.objects.get(product__id=id)
        
        context = header_context(request)
        context.update({
            'title': 'Информация о продукте',
            'product': data,
            'amount': amount,
        })
        
        return render(request, 'petstore/product.html', context)


class OrderView(View):
    def get(self, request, *args, **kwargs):
        context = header_context(request, 'Order')
        
        try: user = request['user']
        except: user = request.user
        
        order = Order.objects.get_or_create(user_id=user.id)[0]
        print(order.products)
        context.update({
            'order': order
        })
        return render(request, 'petstore/order.html', context)
        
    def post(self, request, *args, **kwargs):
        context = header_context(request, 'Order')
        try: user = request['user']
        except: user = request.user
        
        order:Order = Order.objects.get_or_create(user_pk=user.pk)
        context.update({
            'order': order
        })
        return render(request, 'petstore/order.html', context)

class AppendToOrderView(View):
    def get(self, request, product_id):
        request
        context = header_context(request)
        try: user = request['user']
        except: user = request.user
        
        order = Order.objects.get(user_id=user.id)
        context.update({
            'order': order
        })
        product = Product.objects.get(id=product_id)
        order.products.add(product)

        return HttpResponseRedirect('/product/{}'.format(product_id))

class RemoveFromOrderView(View):
    def get(self, request, product_id):
        request
        context = header_context(request)
        try: user = request['user']
        except: user = request.user
        
        order = Order.objects.get(user_id=user.id)
        context.update({
            'order': order
        })
        product = Product.objects.get(id=product_id)
        order.products.remove(product)
        return HttpResponseRedirect('/order/')
        # return render(request, 'petstore/order.html', context)
        