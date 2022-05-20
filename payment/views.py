from enum import IntEnum
import json
import os

import stripe
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.conf import settings

from basket.basket import Basket
# from orders.views import payment_confirmation

@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)
    print('total')
    stripe.api_key='sk_test_51L1ZxxAEgKCl1oTarLLvktdcmx6jMd6WD8yg5eTerXAoBVs96oqx8FcYqBY9l3gWFY38ojF9CUjW16C2broetdtK00mRd4Iqw5'
    intent = stripe.PaymentIntent.create(
        
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )
    return render(request, 'payment/payment.html', {'client_secret': intent.client_secret})
