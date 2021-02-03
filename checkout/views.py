from django.shortcuts import render, redirect, \
    reverse, get_object_or_404, HttpResponse

from django.conf import settings
from django.contrib import messages

from .forms import OrderForm
from .models import Order, OrderLineItem

from cart.contexts import cart_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'There is nothing \
                                 in your cart now!')
        return redirect(reverse('bikes'))
    
    current_cart = cart_contents(request)
    total = current_cart['final_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key

    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key, 
        'client_secret': intent.client_secret,
    }
    
    return render(request, template, context)
