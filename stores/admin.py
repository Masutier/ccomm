from django.contrib import admin
from .models import Store


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'manager', 'phone', 'email')

admin.site.register(Store, StoreAdmin)
