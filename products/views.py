from django.shortcuts import render
from .models import Product


# Create your views here.
def bikes(request):
    """
    A view to return all bikes, showing 3 groups: urban, all-road, road 
    """
    bikes = Product.objects.filter(product_type='BIKES')
    context = {
        'bikes': bikes,
    }    
    
    return render(request, 'products/bikes.html', context)