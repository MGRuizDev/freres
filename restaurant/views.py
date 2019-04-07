from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Guest, BookingInformation, PaymentInformation
from .forms import GuestForm, BookingInformationForm, PaymentInformationForm

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'restaurant/home.html'


def reservations(request):
        guest_form  = GuestForm(request.POST or None)
        booking_form = BookingInformationForm(request.POST or None)
        payment_form = PaymentInformationForm(request.POST or None)
        errors = None
        if all([guest_form.is_valid(), booking_form.is_valid(), payment_form.is_valid()]):
            booking = BookingInformation.objects.create(
                room                = booking_form.cleaned_data.get('room'),
                reservation_date    = booking_form.cleaned_data.get('reservation_date'),
                purpose             = booking_form.cleaned_data.get('purpose'),
                additional_services = booking_form.cleaned_data.get('additional_services'),
                special_request     = booking_form.cleaned_data.get('special_request'),
            )
            payment = PaymentInformation.objects.create(
                method          = payment_form.cleaned_data.get('method'),
                name_on_card    = payment_form.cleaned_data.get('name_on_card'),
                card_number     = payment_form.cleaned_data.get('card_number'),
                expiration_date = payment_form.cleaned_data.get('expiration_date'),
            )
            guest = Guest.objects.create(
                full_name = guest_form.cleaned_data.get('full_name'),
                email     = guest_form.cleaned_data.get('email'),
                phone     = guest_form.cleaned_data.get('phone'),
                city      = guest_form.cleaned_data.get('city'),
                state     = guest_form.cleaned_data.get('state'),
                zip_code  = guest_form.cleaned_data.get('zip_code'),
                company   = guest_form.cleaned_data.get('company'),
                booking_info   = booking,
                payment_info   = payment,
            )
            guest.save
            booking.save
            payment.save
            return redirect('home')
        template_name = 'restaurant/reservations.html'
        context = { 'guest_form': guest_form, 'booking_form': booking_form, 'payment_form': payment_form }
        return render(request, template_name, context)
