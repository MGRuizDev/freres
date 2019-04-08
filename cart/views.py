from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from wineList.models import Wine
from cart.models import Cart, CartItem
# Create your views here.


def view_cart(request):
    template = "cart/view_cart.html"
    try:
        cart_id = request.session['cart_id']
    except:
        cart_id = False
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = False
    try:
        excist = CartItem.objects.filter(cart=cart)
    except:
        excist = False
    return render(request, template, {'cart': cart, 'excist': excist})


def update_cart(request, id):
    try:
        product = Wine.objects.get(id=id)
    except:
        product = False
    try:
        cart_id = request.session['cart_id']
    except:
        cart_id = False
    try:
        cart = Cart.objects.get(id=cart_id)
    except Cart.DoesNotExist:
        cart = Cart()
        cart.save()
        request.session['cart_id'] = cart.id
    if product:
        new_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if created:
            new_item.cart = cart
            new_item.save()
        else:
            new_item.delete()
    return HttpResponseRedirect(reverse('cart:view_cart'))
