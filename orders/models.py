from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, verbose_name=_('FirstName'))
    last_name = models.CharField(max_length=100, verbose_name=_('LastName'))
    email = models.EmailField(verbose_name=_('Email'))

    phone_number = models.CharField(max_length=11, verbose_name=_('PhoneNumber'))
    country = models.CharField(max_length=100, verbose_name=_('Country'))
    city = models.CharField(max_length=100, verbose_name=_('City'))
    address = models.CharField(max_length=700, verbose_name=_('Address'))

    order_notes = models.CharField(max_length=700, verbose_name=_('Notes'), blank=True)
    is_paid = models.BooleanField(default=False)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order: {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'OrderItem: {self.id} Of Order: {self.order.id}'
