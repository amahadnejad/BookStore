from django.urls import path

from .views import order_create_view, order_receipt_view, UserOrdersListView

urlpatterns = [
    path('create/', order_create_view, name='order_create'),
    path('receipt/<int:order_id>/', order_receipt_view, name='order_receipt'),
    path('', UserOrdersListView.as_view(), name='user_orders'),
]
