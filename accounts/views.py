from multiprocessing import context
from turtle import pen
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

# Create your views here.
from .models import *

def home(request):
    return render(request,'accounts/home.html')

def profile(request):
    return render(request, 'accounts/profile.html') 

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer': customer , 'orders': orders, 'order_count':order_count}
    
    return render(request, 'accounts/customer.html', context)

def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'productsLists' : products})    

def dashboard(request):
    # return render(request, 'accounts/dashboard.html')    
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    total_customers = customers.count()
    pending = orders.filter(status='Pending').count()
    delivered = orders.filter(status='Delivered').count()

    # this is a dictionary which allows more than one list
    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders,'total_customers': total_customers,
        'pending': pending, 'delivered': delivered}
                
    return render(request,'accounts/dashboard.html',context)


def createOrder(request):
    form = OrderForm()
    if request.method == "POST":
    #    print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            # this redirect the data the a specific directory 
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance= order)
    if request.method == "POST":
        #    print('Printing POST:', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            # this redirect the data the a specific directory 
            return redirect('/dashboard')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/dashboard')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)

