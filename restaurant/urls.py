from django.urls import path
from.views import HomeTemplateView, reservations

app_name='restaurant'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('reservations/', reservations, name='reservations'),
]
