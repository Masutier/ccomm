from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Store(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    floor = models.DecimalField(max_digits=2, decimal_places=0, null=False, blank=False)
    localNum = models.DecimalField(max_digits=4, decimal_places=0, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    state = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    manager = models.CharField(max_length=60, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    whatsapp = models.CharField(max_length=20, null=True, blank=True)
    webpage = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=100, null=False, blank=False)
    logo = models.ImageField(default='img/logos/default.png', upload_to='img/logos/')
    localFoto = models.ImageField(default='img/locals/logolocal.png', upload_to='img/locals/')
    active = models.BooleanField(default=False, blank=False, null=True)
    outstanding = models.BooleanField(default=True, blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
