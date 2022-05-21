from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from orders.models import Order
from orders.views import user_orders
from store.models import Product

from .forms import RegistrationForm, UserAddressForm
from .models import Address

from orders.views import user_orders

from .forms import RegistrationForm
from .models import UserBase
from .token import account_activation_token


@login_required
def dashboard(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return render(request, "account/user/dashboard.html", {"orders": orders}) 

def account_register(request):

    if request.user.is_authenticated:
        return redirect('account:dashboard')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = True
            user.save()
    else:
        registerForm = RegistrationForm()
    return render(request, 'account/registration/register.html', {'form': registerForm})
    return redirect('account:dashboard')

@login_required
def view_address(request):
    addresses = Address.objects.filter(customer=request.user)
    return render(request, "checkout/delivery_address.html", {"addresses": addresses})

@login_required
def add_address(request):
    if request.method == "POST":
        address_form = UserAddressForm(data=request.POST)
        if address_form.is_valid():
            address_form = address_form.save(commit=False)
            address_form.customer = request.user
            address_form.save()
            return HttpResponseRedirect(reverse("checkout:delivery_address"))
    else:
        address_form = UserAddressForm()
    return render(request, "checkout/add_address_form.html", {"form": address_form})


# @login_required
# def user_orders(request):
#     user_id = request.user.id
#     orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
#     return render(request, "account/user/dashboard.html", {"orders": orders})    
        