from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages

from .forms import PcsForm
from .models import *


def pcs(request):
    compleated = Pcs.objects.filter(pcType='Completo')

    context = {"title": "Pcs", 'compleated':compleated}
    return render(request, "computo/pcs.html", context)


def cpu(request):
    cpus = Pcs.objects.filter(pcType='Cpu')

    context = {"title": "CPU", 'cpus':cpus}
    return render(request, "computo/cpu.html", context)


def laptop(request):
    Laptops = Pcs.objects.filter(pcType='Laptop')

    context = {"title": "Laptops", 'Laptops':Laptops}
    return render(request, "computo/laptop.html", context)


def createPc(request):
    form = PcsForm()
    if request.method == 'POST':
        form = PcsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'El producto ya quedo guardado!')
            return redirect('home')

    context = {"title":"Crear Pc", 'form':form}
    return render(request, "computo/logs/pcform.html", context)


def updatePc(request, pk):
    pcs = Pcs.objects.get(id=pk)
    form = PcsForm(instance=pcs)
    if request.method == 'POST':
        form = PcsForm(request.POST, instance=pcs)
        if form.is_valid():
            form.save()
            messages.success(request, f'El producto ya quedo guardado!')
            return redirect('home')

    context = {"title":"Modificar Pc", 'form':form}
    return render(request, "computo/logs/pcform.html", context)


def delpc(request, pk):
    pcs = Pcs.objects.get(id=pk)
    if request.method == "POST":
        pc.delete()
        messages.success(request, f'El producto se elimino!')
        return redirect('home')
    
    context = {"title":"Eliminar Pc", 'pcs':pcs}
    return render(request, "computo/logs/pcdelete.html", context)
