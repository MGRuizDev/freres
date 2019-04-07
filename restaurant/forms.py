from django import forms
#from django.forms import ModelForm
from .models import Guest, BookingInformation, PaymentInformation

class GuestForm(forms.Form):
        full_name = forms.CharField(max_length=50)
        email     = forms.EmailField(max_length=100)
        phone     = forms.CharField(max_length=15)
        city      = forms.CharField(max_length=50)
        state     = forms.CharField(max_length=20)
        zip_code  = forms.CharField(max_length=10)
        company   = forms.CharField(max_length=100)

class BookingInformationForm(forms.Form):
        area = (
            ('Alamo', 'Alamo'),
            ('Capistrano', 'Capistrano'),
            ('San Jose', 'San Jose'),
            ('Espada', 'Espada'),
            ('Terrace', 'Terrace'),
        )
        addServices = (
            ('food', 'food'),
            ('flowers', 'flowers'),
            ('candels', 'candels'),
            ('valet perking', 'valet parking'),
        )
        room                = forms.CharField(max_length=20, widget=forms.Select(choices=area))
        reservation_date    = forms.DateField()
        purpose   = forms.CharField(max_length=1000, widget=forms.Textarea)
        additional_services = forms.CharField(widget=forms.CheckboxSelectMultiple(choices=addServices))
        special_request = forms.CharField(max_length=1000, widget=forms.Textarea)


class PaymentInformationForm(forms.Form):
        payment = (
            ('debit', 'debit'),
            ('credit','credit'),
        )
        method          = forms.CharField(max_length=6, widget=forms.Select(choices=payment))
        name_on_card    = forms.CharField(max_length=50)
        card_number     = forms.CharField(max_length=20)
        expiration_date = forms.DateField()
