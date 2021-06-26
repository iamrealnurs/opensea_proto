from django.shortcuts import render, get_object_or_404
from main.models import Product

__all__ = (
    'home',
)

def home(request, pk=None):
    if pk:
        product = get_object_or_404(Product, id=pk)
        context = {'object': product}
        return render(request, 'product/detail.html', context)
    qs = Product.objects.all()
    context = {'objects_list': qs}
    return render(request, 'product/home.html', context)

