import random
from datetime import datetime
from django.db import models


class Clients(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField(default=0)
    date_registration = models.DateField(auto_now=True)


class Product(models.Model):
    name_product = models.CharField(max_length=100)
    product_description = models.TextField()
    price = models.DecimalField(max_length=0, max_digits=2, decimal_places=0)
    count = models.IntegerField(default=0)
    create_date_product = models.DateField(auto_now=True)


class Order(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_add = models.DecimalField(max_length=0, max_digits=2, decimal_places=0)
    date_order = models.DateField(auto_now=True)



