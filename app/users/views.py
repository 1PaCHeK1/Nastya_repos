from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.conf import settings
from django.core.mail import send_mail

from app.utils import header_context
from .forms import RegistrationForm
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin    
)
from .models import (
    User
)
from .serializers import UserSerializer

def send_mail_to_user(user: User, title, message):
    send_mail(title, message, settings.EMAIL_HOST_USER, [user.email])

def send_mail_to_users(title, message, users=None):
    if not users:
        users = User.objects.filter(receive_newsletter=0)
    send_mail(title, message, settings.EMAIL_HOST_USER, [user.email for user in users])

# users = User.objects.all()
# send_mail_to_users('тайтл', 'какое-то сообщение', users)



class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        
        form = RegistrationForm()
        context = header_context(request)
        context.update({
            'form': form
        })
        return render(request, 'users/registration.html', context)
    
    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        context = header_context(request)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/login/')
        else:
            context.update({
                'form': form
            })
            return render(request, 'users/registration.html', context)

class HelloWorldView(View):
    def get(self, request, *args, **kwargs):
        context = header_context(request)
        context = {
            'title': 'Hello page',
            'name': 'sdkjfbsdg'
        }

        return render(request, 'users/index.html', context)

class UsersJSONView(RetrieveModelMixin,
                    ListModelMixin,
                    GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProfileView(View):
    @method_decorator(login_required())
    def get(self, request, *args, **kwargs):
        context = header_context(request)
        try: user = request.user
        except: user = request['user']
        context.update({
            'title': 'Hello page',
            'name': 'sdkjfbsdg',
            'form': RegistrationForm,
            'user': user
        })
        
        return render(request, 'users/profile.html', context)