from django.shortcuts import render

# Create your views here.
def bikes(request):
    """
    A view to return all bikes, showing 3 groups: urban, all-road, road 
    """
    return render(request, 'products/bikes.html', context)