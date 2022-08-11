from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import Customer, Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class UpdateOrder(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'