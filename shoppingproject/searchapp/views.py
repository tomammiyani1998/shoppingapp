from django.shortcuts import render
from shoppingapp.models import Product
from django.db.models import Q

# Create your views here.


def searchapp(request):
    if 'q' in request.GET:
        query = request.GET.get('q')
        if query == "":
            query = None
            products = None
            return render(request, 'search.html', {'query': query, 'products': products})
        else:
            products = Product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
            return render(request, 'search.html', {'query': query, 'products': products})