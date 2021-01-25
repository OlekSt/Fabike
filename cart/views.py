from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """ A view to return shopping card page """
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    product = get_object_or_404(Product, pk=item_id)
    # to get a chosen combination of a product + color + size + components(for bikes, and none for frames)
    size = request.POST.get('size')
    color = request.POST.get('color')
    if 'components' in request.POST:
        components = request.POST['components']
    else:
        components = 'none'

    # options_in_cart to check if such a combination has been added to the cart
    options_to_add = (size, color, components)
    options_in_cart = "-".join(options_to_add)

    cart = request.session.get('cart', {})
    if item_id in list(cart.keys()):
        if options_in_cart in cart[item_id]['items_by_options'].keys():
            cart[item_id]['items_by_options'][options_in_cart] += quantity
            if components == 'none':
                messages.success(request, f'Updated quantity of {product.frame} {product.name} in {color} color &  size {size} in your bag')
            else:
                messages.success(request, f'Updated quantity of {product.name} with {product.frame} frame & {components} components in {color} color, size {size} in your bag')
        else:
            cart[item_id]['items_by_options'][options_in_cart] = quantity
            if components == 'none':
                messages.success(request, f'Added {product.frame} {product.name} in {color} color & {size} size in your bag')
            else:
                messages.success(request, f'Added {product.name} with {product.frame} frame & {components} components in {color} color, size {size} to your bag')
    else:
        cart[item_id] = {'items_by_options': {options_in_cart: quantity}}
        if components == 'none':
            messages.success(request, f'Added {product.frame} {product.name} in {color} color & size {size} to your bag')
        else:
            messages.success(request, f'Added {product.name} with {product.frame} frame & {components} components in {color} color, size {size} to your bag')

    request.session['cart'] = cart

    return redirect(redirect_url)
