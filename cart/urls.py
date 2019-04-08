from django.urls import path
from .views import update_cart, view_cart

app_name='cart'

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('update/<id>', update_cart, name='update_cart'),
]
