from django.db import models
from django.forms import ModelForm
from django import forms
from .models import *


class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = '__all__'
