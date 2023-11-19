from django.contrib import admin
from .models import AppleStore, Order

#username apple
admin.site.register(AppleStore)
admin.site.register(Order)