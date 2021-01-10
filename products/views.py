from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


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
