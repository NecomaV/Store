from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import (UserLoginForm)
from django.views.generic import TemplateView
from .forms import  UserLoginForm
from . import views





app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/registration/login.html',
                                                form_class=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),                                            
    path('register/', views.account_register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("add_address/", views.add_address, name="add_address"),
    path("addresses/", views.view_address, name="addresses"),
    # path("user_orders/", views.user_orders, name="user_orders"),
  
    
]