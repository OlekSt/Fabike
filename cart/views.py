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

    if components:
        if item_id in list(cart.keys()):
            if components in cart[item_id]['components_type'].keys():
                cart[item_id]['components_type'][components] += quantity
            else:
                cart[item_id]['components_type'][components] = quantity
        else:
            cart[item_id] = {'components_type': {components: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity
    
   # product = get_object_or_404(Product, pk=item_id)
    #if components:
    #    if components == 'carbon':
    #        price = product.price_carbon
    #    else: 
    #        price = product.price_alloy
    #else:
    #    price = product.price
        
    request.session['cart'] = cart
    print(cart)
    print(request.session['cart'])
    print(components)
    print(size)
    print(color)
    
    return redirect(redirect_url)
