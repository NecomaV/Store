
from django.urls import path



app_name = 'account'

urlpatterns = [
    path('register/', views.account_register, name='register'),
]