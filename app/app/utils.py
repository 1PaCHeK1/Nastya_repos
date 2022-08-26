from petstore.models import (
    ProductType
)


def header_context(request, title='') -> dict:
    context = {
        'title': title,
        'producttypes': ProductType.objects.all()
    }
    return context 