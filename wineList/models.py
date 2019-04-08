from django.db import models

# Create your models here.

class Wine(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000, help_text='Enter a brief description')
    designation = models.CharField(max_length=200, null=True, blank=True)
    points = models.CharField(max_length=20, null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    province =models.CharField(max_length=200, null=True, blank=True)
    region = models.CharField(max_length=200, null=True, blank=True)
    subregion = models.CharField(max_length=200, null=True, blank=True)
    variety = models.CharField(max_length=200, null=True, blank=True)
    winery = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        # String for representing the model object
        return self.winery
