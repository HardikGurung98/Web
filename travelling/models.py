from django.db import models

# Create your models here.
class travelling(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    features = models.TextField()
    price = models.FloatField()

class BookNow(models.Model):
    Fn = models.CharField(max_length=100, default="")
    Ln = models.CharField(max_length=100, default="")
    un = models.CharField(max_length=100, default="")
    cty = models.CharField(max_length=100, default="")
    zp = models.FloatField()
