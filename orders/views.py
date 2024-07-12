from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext as _

from cart.cart import Cart
from .forms import OrderForm
from .models import OrderItem, Order


@login_required
def order_create_view(request):
    order_form = OrderForm()
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, _('You can not proceed to checkout page because your cart is empty.'))
        return redirect('book_list')

    if request.method == 'POST':
        order_form = OrderForm(request.POST, )

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                book = item['book_obj']
                OrderItem.objects.create(
                    order=order_obj,
                    book=book,
                    quantity=item['quantity'],
                    price=book.price,
                )

            cart.clear()

            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()

            request.session['order_id'] = order_obj.id
            messages.success(request, _("Your Order Successfully Placed"))
            return redirect('order_receipt', order_obj.id)

    return render(request, 'orders/order_create.html', {
        'form': order_form,
    })


@login_required
def order_receipt_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = OrderItem.objects.filter(order=order)

    return render(request, 'orders/order_receipt.html', {
        'order': order,
        'order_items': order_items,
    })