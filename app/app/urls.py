"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.conf import settings
import users.views as user_view 
import petstore.views as petstore_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # USERS
    path('hello/', user_view.HelloWorldView.as_view(), name='hello-page'),
    path('registration/', user_view.RegistrationView.as_view(), name='registration'),

    # PETSTORE
    path('products/', petstore_view.ProductsView.as_view(), name='products-page'),
    path('product/<int:id>', petstore_view.ProductView.as_view(), name='product-page'),
    path('order/', petstore_view.OrderView.as_view(), name='order'),
    path('appendToOrder/<int:product_id>', petstore_view.AppendToOrderView.as_view(), name='append-order'),
    path('removeFromOrder/<int:product_id>', petstore_view.RemoveFromOrderView.as_view(), name='remove-order'),

    ### AUTH
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', user_view.ProfileView.as_view(), name='profile'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)