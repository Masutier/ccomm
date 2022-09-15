from django.db import models
from django.forms import ModelForm
from django import forms
from stores.models import *
from .models import *


class PcsForm(ModelForm):
    class Meta:
        model = Pcs
        fields = '__all__'
