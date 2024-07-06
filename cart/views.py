from django.shortcuts import render, get_object_or_404, redirect

from .cart import Cart
from books.models import Book
from .forms import AddToCartBookForm


def cart_detail_view(request):
    cart = Cart(request)

    return render(request, 'cart/cart_detail.html', {
        'cart': cart,
    })


