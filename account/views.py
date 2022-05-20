from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required   
from django.http import HttpResponse
from django.shortcuts import redirect, render


# from orders.views import user_orders

from .forms import RegistrationForm, UserEditForm
from .models import UserBase
from .token import account_activation_token


@login_required
def dashboard(request):
    return render(request,
                  'account/user/dashboard.html')
                 


# @login_required
# def edit_details(request):
#     if request.method == 'POST':
#         user_form = UserEditForm(instance=request.user, data=request.POST)

#         if user_form.is_valid():
#             user_form.save()
#     else:
#         user_form = UserEditForm(instance=request.user)

#     return render(request,
#                   'account/user/edit_details.html', {'user_form': user_form})


@login_required
def delete_user(request):
    user = UserBase.objects.get(user_name=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return render(request,'account/user/delete_account.html')
    return redirect('account:delete_confirm')


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

        