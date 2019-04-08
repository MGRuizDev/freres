from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch.dispatcher import receiver
from wineList.models import Wine

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    total = models.DecimalField(max_digits=50, default=0, decimal_places=2)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.id)

class CartItem(models.Model):
    product = models.ForeignKey(Wine, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.winery

@receiver([signals.post_save, signals.post_delete], sender=CartItem)
def update_cart_total(sender, instance, **kwargs):
    cart = instance.cart
    totals = [item.product.price for item in cart.cartitem_set.all()]
    cart.total = sum(totals)
    cart.save()
