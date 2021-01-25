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
                color = options[0]
                size = options[1]
                components = options[2]
                if components == 'alloy':
                    price = product.price_alloy
                elif components == 'carbon':
                    price = product.price_carbon
                else:
                    price = product.price
                total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'color': color,
                    'size': size,
                    'components': components,
                })

    context = {
        'cart_items': cart_items, 
        'total': total,
        'product_count': product_count,
    }

    return context
