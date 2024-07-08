from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'country', 'city', 'address', 'order_notes', ]
        widgets = {
            'order_notes': forms.Textarea(attrs={'rows': 5, 'placeholder': 'If You Have Any Notes Please Leave It Here'}),
            'address': forms.Textarea(attrs={'rows': 3})

        }