from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import StoreForm
from .models import *


def stores(request):
    stores = Store.objects.all()

    context = {"title": "Stores", 'stores':stores}
    return render(request, "stores/stores.html", context)


def createStore(request):
    form = StoreForm()
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'El Almacen ya se creo!')
            return redirect('home')

    context = {"title": "Crear Store", 'form':form}
    return render(request, "stores/logs/storeform.html", context)


def updateStore(request, pk):
    store = Store.objects.get(id=pk)
    form = StoreForm(instance=store)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            messages.success(request, f'La Tienda quedo guardada!')
            return redirect('stores')
    
    context = {"title": "Modificar Store", 'form':form}
    return render(request, "stores/logs/storeform.html", context)
