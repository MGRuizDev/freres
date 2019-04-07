from django.contrib import admin
from .models import Guest, BookingInformation, PaymentInformation
# Register your models here.

admin.site.register(Guest)
admin.site.register(BookingInformation)
admin.site.register(PaymentInformation)
