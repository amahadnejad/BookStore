from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from .cart import Cart
from books.models import Book
from .forms import AddToCartBookForm


def cart_detail_view(request):
    # Getting Cart
    cart = Cart(request)

    # Loop Through The Cart
    for item in cart:
        item['book_update_quantity_form'] = AddToCartBookForm(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })

    return render(request, 'cart/cart_detail.html', {
        'cart': cart,
    })


@require_POST
def add_to_cart_view(request, book_id):
    # Getting Cart
    cart = Cart(request)
    # Getting Book
    book = get_object_or_404(Book, id=book_id)
    form = AddToCartBookForm(request.POST)

    # Clean Data And Add To Cart
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        # Check stock availability
        if book.stock >= quantity:
            cart.add(book, quantity, replace_current_quantity=cleaned_data['inplace'])
            book.stock -= quantity  # Decrease the stock
            book.save()  # Save the changes
        else:
            messages.warning(request, _("Sorry! This quantity is not available in our warehouse"))

    return redirect('cart:cart_detail')


def remove_from_cart(request, book_id):
    # Getting Cart
    cart = Cart(request)
    # Getting Book
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)

    return redirect('cart:cart_detail')


def clear_cart(request):
    # Getting Cart
    cart = Cart(request)

    # Clear Cart If It Has Products
    if len(cart):
        cart.clear()
        messages.success(request, _('All products successfully removed from your cart'))
    else:
        messages.warning(request, _('Your cart is already empty'))
    return redirect('cart:cart_detail')
