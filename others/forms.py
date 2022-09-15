from django.db import models
from django.forms import ModelForm
from django import forms
from .models import *


class OtherForm(ModelForm):
    class Meta:
        model = Others
        fields = '__all__'
