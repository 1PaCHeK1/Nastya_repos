from urllib import request
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, JsonResponse
 
from app.utils import header_context
from django.contrib.auth.decorators import login_required

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin    
)

from .serializers import (
    OrderSerializer, 
    OrderCreateSerializer,
    ProductSerializer
)
from .models import (
    Product, 
    ProductAmounts, 
    Order
)

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

class ProductsJSONView(RetrieveModelMixin,
                    ListModelMixin,
                    CreateModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin,
                    GenericViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        return ProductSerializer


class OrderView(View):
    def get(self, request, *args, **kwargs):
        context = header_context(request, 'Order')
        return render(request, 'petstore/order.html', context)

    def post(self, request, *args, **kwargs):
        context = header_context(request, 'Order')
        return render(request, 'petstore/order.html', context)


class OrderJSONView(RetrieveModelMixin,
                    ListModelMixin,
                    CreateModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin,
                    GenericViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        else:
            return OrderSerializer