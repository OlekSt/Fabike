from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from . import views


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, options_in_cart in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        for options, quantity in options_in_cart['items_by_options'].items():
            options = options.split('-')
            color = options[1]
            size = options[2]
            components = options[3]
            if components == 'alloy':
                price = product.price_alloy
            elif components == 'carbon':
                price = product.price_carbon
            else:
                price = product.price
            price = int(price)
            quantity = int(quantity)
            total += quantity * price
            product_count += quantity
            item_in_cart = "-".join(options)
            cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'color': color,
                'item_in_cart': item_in_cart,
                'size': size,
                'components': components,
                'price': price,
            })
        
    delivery = 0
    final_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'delivery': delivery,
        'final_total': final_total,
        'product_count': product_count,
    }

    return context
