from django import forms


class AddToCartBookForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, required=True)
    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput)
