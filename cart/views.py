from django.shortcuts import render


def view_cart(request):
    """ A view to return shopping card page """
    return render(request, 'cart/cart.html')
