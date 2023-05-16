from django.db import models


class Product(models.Model):
    objects = None
    title = models.CharField(max_length=64)
    date_receipt = models.DateTimeField()
    price = models.FloatField()
    measure_unit = models.IntegerField()
    provider = models.CharField(max_length=64)
