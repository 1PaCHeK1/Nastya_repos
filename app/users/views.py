from django.shortcuts import render

# Create your views here.
def hello_world(request):
    context = {
        'title': 'Hello page',
        'name': 'sdkjfbsdg'
    }

    return render(request, 'users/index.html', context)