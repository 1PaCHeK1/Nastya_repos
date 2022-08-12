from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from app.utils import header_context


# Create your views here.
def hello_world(request):
    context = header_context(request)
    context = {
        'title': 'Hello page',
        'name': 'sdkjfbsdg'
    }

    return render(request, 'users/index.html', context)


@login_required
def profile(request):
    context = header_context(request)
    context.update({
        'title': 'Hello page',
        'name': 'sdkjfbsdg'
    })
    
    return render(request, 'users/profile.html', context)