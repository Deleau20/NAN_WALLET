from django.contrib import admin
from .models import Profile, PaymentMethod, Account, Bank, Transaction

admin.site.register(Profile)
admin.site.register(PaymentMethod)
admin.site.register(Account)
admin.site.register(Bank)
admin.site.register(Transaction)