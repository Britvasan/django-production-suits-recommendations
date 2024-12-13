from django import forms
from .models import Clientdata
from datetime import date
from django.utils import timezone

class ClientdataForm(forms.ModelForm):
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 1:
            raise forms.ValidationError("Quantity must be at least 1.")
        return quantity

    def clean_pickup_date(self):
        pickup_date = self.cleaned_data.get('pickup_date')
        # if pickup_date < timezone.now().date():
        if pickup_date and pickup_date < date.today():
            raise forms.ValidationError("Pickup date cannot be in the past.")
        return pickup_date

    class Meta:
        model = Clientdata
        fields = ['client_name', 'phone_number', 'email', 'orders', 'order_type', 'customization', 'quantity', 'pickup_date']










# from django import forms
# from .models import Clientdata

# class ClientdataForm(forms.ModelForm):
#     class Meta:
#         model = Clientdata
#         fields = ['client_name', 'phone_number', 'email', 'order', 'order_type', 'customization', 'quantity', 'pickup_date']





