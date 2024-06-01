from django.db import models

class Price(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)

class FDData(models.Model):
    name = models.CharField(max_length=100)
    production = models.DecimalField(max_digits=10, decimal_places=2)
    consumption = models.DecimalField(max_digits=10, decimal_places=2)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    production = models.DecimalField(max_digits=10, decimal_places=2)
    consumption = models.DecimalField(max_digits=10, decimal_places=2)
    ID_FD = models.IntegerField()