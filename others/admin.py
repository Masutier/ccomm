from django.contrib import admin
from .models import Others


class OthersAdmin(admin.ModelAdmin):
    list_display = ('name', 'clotesType', 'cost', 'price', 'discount')

admin.site.register(Others, OthersAdmin)
