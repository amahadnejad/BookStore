from django.db import models
from django.conf import settings


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=100, verbose_name='FirstName')
    last_name = models.CharField(max_length=100, verbose_name='LastName')
    email = models.EmailField(verbose_name='Email')

    phone_number = models.CharField(max_length=11, verbose_name='PhoneNumber')
    country = models.CharField(max_length=100, verbose_name='Country')
    city = models.CharField(max_length=100, verbose_name='City')
    address = models.CharField(max_length=700, verbose_name='Address')

    order_notes = models.CharField(max_length=700, verbose_name='Notes')
    is_paid = models.BooleanField(default=False)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order: {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey('books.Book', on_delete=models.PROTECT, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'OrderItem: {self.id} Of Order: {self.order.id}'
