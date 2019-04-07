from django.db import models

# Create your models here.

class Wine(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    country = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Enter a brief description')
    designation = models.CharField(max_length=200)
    points = models.CharField(max_length=20)
    price = models.CharField(max_length=30)
    province =models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    subregion = models.CharField(max_length=200)
    variety = models.CharField(max_length=200)
    winery = models.CharField(max_length=200)

    def __str__(self):
        # String for representing the model object
        return self.winery