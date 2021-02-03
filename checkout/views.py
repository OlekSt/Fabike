from django.shortcuts import render, redirect, \
    reverse, get_object_or_404, HttpResponse

from django.conf import settings
from django.contrib import messages

from .forms import OrderForm
from .models import Order, OrderLineItem

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'There is nothing \
                                 in your cart now!')
        return redirect(reverse('bikes'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Hnkf4DOLZlnTmDnah8NE9Ru9GN9jzDgDcanvTPLmxeungfmPQbwEKC3pHO4SkiYZbEZwHCM2TvHMR1ISXxte9uf00iNiobEit', 
        'client_secret': 'test client secret',
    }
    
    return render(request, template, context)
