from django.contrib import admin

from .models import UserBase
from .models import Address

admin.site.register(UserBase)
admin.site.register(Address)
