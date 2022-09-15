from django.db import models
from django.forms import ModelForm
from django import forms
from stores.models import *
from .models import *


class MonitorForm(ModelForm):
    class Meta:
        model = Monitor
        fields = '__all__'
