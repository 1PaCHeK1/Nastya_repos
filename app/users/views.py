from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from app.utils import header_context
from .forms import RegistrationForm

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