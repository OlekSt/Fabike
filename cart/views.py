from django.shortcuts import render


def view_cart(request):
    """ A view to return shopping card page """
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('size')
    color = request.POST.get('color')
    components = request.POST.get('components')
    cart = request.session.get('cart', {})

   
    cart[item_id] = quantity
        
    
    request.session['cart'] = cart
    print(request.session['cart'])
    
    
    return redirect(redirect_url)