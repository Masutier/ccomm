from django.contrib import admin
from .models import *


class VisualAdmin(admin.ModelAdmin):
    list_display = ('name', 'store', 'cost', 'label', 'price', 'discount')

admin.site.register(Monitor, VisualAdmin)
