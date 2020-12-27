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


def bike(request, product_id):
    """
    A view to return an individual bike details
    """
    bikes = Product.objects.filter(product_type='BIKES')
    bike = get_object_or_404(bikes, pk=product_id)
    context = {
        'bike': bike,
    }    
    return render(request, 'products/bike.html', context)


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

def frame(request, product_id):
    """
    A view to return an individual bike details
    """
    frames = Product.objects.filter(product_type='FRAMES')
    frame = get_object_or_404(frames, pk=product_id)
    context = {
        'frame': frame,
    }    
    return render(request, 'products/frame.html', context)


def carbon(request):
    """
    A view to return carbon fibre page
    """
    carbon = Product.objects.filter(product_group='CARBON')
    carbon = get_object_or_404(carbon)
    context = {
        'carbon': carbon,
    }    
    return render(request, 'products/carbon.html', context)


def titanium(request):
    """
    A view to return titanium frame page
    """
    titanium = Product.objects.filter(product_group='TITANIUM')
    titanium = get_object_or_404(titanium)
    context = {
        'titanium': titanium,
    }    
    
    return render(request, 'products/titanium.html', context)

