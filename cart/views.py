from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from products.models import Product


def view_cart(request):
    """ A view to return shopping card page """
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = 1
    redirect_url = request.POST.get('redirect_url')

    size = request.POST.get('size')
    color = request.POST.get('color')

    components = None
    if 'components' in request.POST:
        components = request.POST['components']
    cart = request.session.get('cart', {})

    
    request.session['cart'] = cart
    print(cart)
    print(request.session['cart'])
    print(size)
    print(color)
    
    return redirect(redirect_url)
