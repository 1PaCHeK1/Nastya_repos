from http.client import ResponseNotReady
from urllib import request
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, JsonResponse
 
from app.utils import header_context
from django.contrib.auth.decorators import login_required

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
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
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        else:
            return OrderSerializer
        
from django.db.models import F, Q, Sum, Count, Max, Min, Subquery, OuterRef, Case, When

class GetAllProductStat(ListModelMixin,
                    GenericViewSet):
    
    permission_classes = (AllowAny,)
    
    def list(self, request, *args, **kwargs):
        # orders = (Order.objects
        #             .filter(Q(status=0)
        #                     & Q(products__product_id=3)).values("products__product_id", "order_id", "status"))
        # print(orders)
        products = (Product.objects
                    .select_related('type', 'productamounts', 'orders')
                    .annotate(total_buyed=Sum(Case(
                        When(order__status=0, then=1), 
                        default=0
                    )))
                    .annotate(amount=Sum("productamounts__amount"))
                    .values("name", "price", "type__type", "productamounts__amount", "total_buyed")
                    )
        return Response(products)
