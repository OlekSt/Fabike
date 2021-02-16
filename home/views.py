from django.shortcuts import render


def index(request):
    """ A view to return index page """
    return render(request, 'home/index.html')


def under_construction(request):
    """ A view to return a page which is to be added """
    return render(request, 'home/under_construction.html')
