from django.shortcuts import render, redirect, reverse,\
                                get_object_or_404, HttpResponse
from django.contrib import messages
from products.models import Product
from django import template
from decimal import Decimal


def view_cart(request):
    """ A view to return shopping card page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    product = get_object_or_404(Product, pk=item_id)
    # to get a chosen combination of a product + color + size +
    # components(for bikes, and none for frames)
    size = request.POST.get('size')
    color = request.POST.get('color')
    if 'components' in request.POST:
        components = request.POST['components']
    else:
        components = 'none'
    # options_in_cart to check if such a combination has been added to the cart
    item_to_add = (item_id, color, size, components)
    item_in_cart = "-".join(item_to_add)

    cart = request.session.get('cart', {})
    if item_id in list(cart.keys()):
        if item_in_cart in cart[item_id]['items_by_options'].keys():
            cart[item_id]['items_by_options'][item_in_cart] += quantity
            if components == 'none':
                messages.success(request, f'Updated quantity of {product.frame} \
                {product.name} in {color} color &  size {size} in your cart')
            else:
                messages.success(request, f'Updated quantity of {product.name} with\
                {product.frame} frame   in {color} color, size {size} with \
                {components} components in your cart')
        else:
            cart[item_id]['items_by_options'][item_in_cart] = quantity
            if components == 'none':
                messages.success(request, f'Added {product.frame} {product.name} in\
                {color} color, size {size} to your cart')
            else:
                messages.success(request, f'Added {product.name} with\
                {product.frame} frame in {color} color, size {size}\
                with {components} components to your cart')
    else:
        cart[item_id] = {'items_by_options': {item_in_cart: quantity}}
        if components == 'none':
            messages.success(request, f'Added {product.frame} {product.name}\
            in {color} color, size {size} to your cart')
        else:
            messages.success(request, f'Added {product.name} with\
            {product.frame} frame in {color} color, size {size}\
            with {components} components to your cart')

    request.session['cart'] = cart
    print(cart)
    return redirect(redirect_url)


def update_cart(request, item_id):
    """Update quantity of a specific product in the shopping cart"""

    quantity = request.POST.get('quantity')
    product = get_object_or_404(Product, pk=item_id)
    cart = request.session.get('cart', {})

    for item_in_cart in cart[item_id]['items_by_options'].keys():
        if request.method == 'POST':
            btn_update = f'update_{item_in_cart}'
            if btn_update in request.POST:
                cart[item_id]['items_by_options'][item_in_cart] = quantity

    messages.success(request, f'Updated quanitity of {product.frame}\
        {product.name} to { quantity } in your cart')
    request.session['cart'] = cart
    print(cart)
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove a specific product from the shopping cart"""

    product = Product.objects.get(pk=item_id)
    cart = request.session.get('cart', {})

    for cart_items, items_by_options in cart.items():
        for value in items_by_options.values():
            for item_in_cart, key in cart[item_id]['items_by_options'].items():
                # to prevent the same button remove
                # several options related to 1 product_id
                btn_remove = f'remove_{item_in_cart}'
                if btn_remove in request.POST:
                    btn_item = btn_remove.split('_')
                    item_to_remove = btn_item[1]
    """
    To remove (pop) a product if there is only 1 product_id +
    1 options variation or to remove only 1 variation
    from several if 1 product_id + several sets of options
    """
    if len(value) == 1 and btn_remove in request.POST:
        cart.pop(item_id)
    else:
        del cart[item_id]['items_by_options'][item_to_remove]

    request.session['cart'] = cart
    print(cart)
    return redirect(reverse('view_cart'))
