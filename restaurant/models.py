from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Guest(models.Model):
    full_name = models.CharField(max_length=50)
    email     = models.EmailField(max_length=100)
    phone     = models.CharField(max_length=15)
    city      = models.CharField(max_length=50)
    state     = models.CharField(max_length=20)
    zip_code  = models.CharField(max_length=10)
    company   = models.CharField(max_length=50)
    booking_info    = models.OneToOneField('BookingInformation', on_delete='CASCADE', null=True, blank=True)   #Strings because they are not defined yet in the script
    payment_info    = models.OneToOneField('PaymentInformation', on_delete='CASCADE', null=True, blank=True)

class BookingInformation(models.Model):
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
    room                = models.CharField(max_length=15, choices=area)
    reservation_date    = models.DateField()
    purpose   = models.TextField(max_length=1000)
    additional_services = MultiSelectField(choices=addServices, null=True, blank=True)
    special_request = models.TextField(max_length=1000)

class PaymentInformation(models.Model):
    payment = (
        ('debit', 'debit'),
        ('credit','credit'),
    )
    method          = models.CharField(max_length=6, choices=payment)
    name_on_card    = models.CharField(max_length=30)
    card_number     = models.CharField(max_length=20)
    expiration_date = models.DateField()
