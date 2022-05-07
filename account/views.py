from atexit import register
from urllib import request
from django.shortcuts import redirect, render

from .forms import RegistrationForm

def account_register(required):
        
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.is_active = False
            user.save()
