from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MonitorForm
from .models import Monitor


def monitors(request):
    monitor = Monitor.objects.all()

    context = {'title': 'Monitores', 'monitor':monitor}
    return render(request, 'visual/monitors.html', context)


def createMonitor(request):
    form = MonitorForm()
    if request.method == 'POST':
        form = MonitorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'El producto ya quedo guardado!')
            return redirect('monitors')

    context = {"title":"Crear Monitor", 'form':form}
    return render(request, "visual/logs/monitorform.html", context)


def updateMonitor(request, pk):
    monitor = Monitor.objects.get(id=pk)
    form = MonitorForm(instance=monitor)
    if request.method == 'POST':
        form = MonitorForm(request.POST, instance=monitor)
        if form.is_valid():
            form.save()
            messages.success(request, f'El producto ya quedo guardado!')
            return redirect('home')

    context = {"title":"Modificar Monitor", 'form':form}
    return render(request, "visual/logs/monitorform.html", context)


def delMonitor(request, pk):
    monitor = Monitor.objects.get(id=pk)
    monitor.delete()
    messages.success(request, f'El Monitor se elimino!')
    return redirect('home')

