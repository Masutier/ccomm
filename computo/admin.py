from django.contrib import admin
from .models import Pcs


class CompuAdmin(admin.ModelAdmin):
    list_display = ('name', 'pcType', 'label', 'store', 'cost', 'price', 'discount')

admin.site.register(Pcs, CompuAdmin)
