from django.urls import path
from .views import *
app_name='wineList'
urlpatterns = [
    path('', home, name='home'),
    path('grapes/<slug>', grapes, name='grapes'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('store/', store, name='store'),
    path('listWine/<slug>', listWine, name='listWine'),
    path('pairing/', pairing, name='pairing'),
]
