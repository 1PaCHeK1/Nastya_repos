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
# from django.contrib.auth.urls
from rest_framework import routers
from django.conf import settings


import users.views as user_view 
import petstore.views as petstore_view
import blog.views as blog_view
import chat.views as chat_views

router = routers.DefaultRouter()

router.register('order-json', petstore_view.OrderJSONView, basename='order-json')
router.register('products-json', petstore_view.ProductsJSONView, basename='products-json')
router.register('users-json', user_view.UsersJSONView, basename='products-json')
router.register('comments-json', blog_view.CommentsJSONView, basename='comments-json')
router.register('get-stat', petstore_view.GetAllProductStat, basename='get-stat')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('summernote/', include('django_summernote.urls')),
    
    
    # USERS
    path('hello/', user_view.HelloWorldView.as_view(), name='hello-page'),
    path('registration/', user_view.RegistrationView.as_view(), name='registration'),

    # PETSTORE
    path('products/', petstore_view.ProductsView.as_view(), name='products-page'),
    path('product/<int:id>', petstore_view.ProductView.as_view(), name='product-page'),
    path('order/', petstore_view.OrderView.as_view(), name='order'),
    
    # AUTH
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', user_view.ProfileView.as_view(), name='profile'),
    
    # BLOG    
    path('blog/', blog_view.BlogListView.as_view(), name='blog-page'),
    path('article/<slug:slug>', blog_view.ArticleDetailView.as_view(), name='article'),
    
    # CHAT
    path('chat', chat_views.chat, name='Chat'),
]

urlpatterns += router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
