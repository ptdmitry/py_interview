from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=64)
    date_receipt = models.DateTimeField()
    price = models.FloatField()
    measure_unit = models.IntegerField()
    provider = models.CharField(max_length=64)
