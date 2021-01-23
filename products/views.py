from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

def products(request):

    products = Product.objects.all()
    query = None
    
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            query = Q(name__icontains=query)  | Q(title__icontains=query) | Q(frame__icontains=query) | Q(fork__icontains=query)  | Q(wheels__icontains=query) | Q(tyres__icontains=query) | Q(crankset__icontains=query)  | Q(shift_levers__icontains=query) | Q(casette_or_sprocket__icontains=query) | Q(chain_or_belt__icontains=query)  | Q(brakes__icontains=query) | Q(bottom_bracket__icontains=query) | Q(dropouts__icontains=query)

            products = products.filter(query)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def bikes(request):
    """
    A view to return all bikes, showing 3 groups: urban, all-road, road 
    """
    urban = Product.objects.filter(product_group='URBAN')
    all_road = Product.objects.filter(product_group='ALL ROAD')
    road = Product.objects.filter(product_group='ROAD')
    context = {
        'urban': urban,
        'all_road': all_road,
        'road': road,    
    }    
    return render(request, 'products/bikes.html', context)


def product(request, product_id):
    """
    A view to return an individual bike details
    """
    products = Product.objects.all()
    product = get_object_or_404(products, pk=product_id)
    context = {
        'product': product,
    }    
    return render(request, 'products/product.html', context)


def urban(request):
    """
    A view to return urban bikes 
    """    
    urban = Product.objects.filter(product_group='URBAN')
    context = {
        'urban': urban,
    }    
    return render(request, 'products/urban.html', context)


def all_road(request):
    """
    A view to return all road bikes 
    """
    all_road = Product.objects.filter(product_group='ALL ROAD')
    context = {
        'all_road': all_road,
    }    
    return render(request, 'products/all_road.html', context)


def road(request):
    """
    A view to return road bikes 
    """
    road = Product.objects.filter(product_group='ROAD')
    context = {
        'road': road,
    }    
    return render(request, 'products/road.html', context)


def frames(request):
    """
    A view to return frames
    """
    frames = Product.objects.filter(product_type='FRAMES')
    context = {
        'frames': frames,
    }    
    return render(request, 'products/frames.html', context)
