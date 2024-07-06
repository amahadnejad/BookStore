from django.urls import path, include

from .views import cart_detail_view, add_to_cart_view, remove_from_cart

app_name = 'cart'

urlpatterns = [
    path('', cart_detail_view, name="cart_detail"),
    path('add/<int:book_id>/', add_to_cart_view, name="cart_add"),
    path('remove/<int:book_id>/', remove_from_cart, name="cart_remove"),

]
