from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm, CustomerForm

def home(request):
    customers  = Customer.objects.all()
    orders = Order.objects.all()

    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()

    context = {'customers':customers, 'orders':orders, 'total_orders':total_orders, 'delivered':delivered,'pending':pending }
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products':products})


def customer(request, pk):
    customer = Customer.objects.get(id = pk)
    orders = customer.order_set.all()
    orders_count = orders.count()

    context = {'customer':customer, 'orders':orders, 'orders_count':orders_count}
    return render(request, 'accounts/customer.html', context)

def createOrder(request):

    form  = OrderForm()
    if request.method == 'POST':
        form  = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'accounts/create_order.html', context)

def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/create_customer.html', context)

