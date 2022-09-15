from django.shortcuts import render

from .forms import OtherForm
from .models import Others


def caps(request):
    other = Others.objects.all()
    print(other)

    context = {"title": "caps", 'other':other}
    return render(request, "others/caps.html", context)


def createCap(request):
    other = Others.objects.all()
    if request.method == 'POST':
        form = OtherForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, f'El producto ya quedo guardado!')
            return redirect('others')
    else:
        form = OtherForm()

    context = {"title": "Crear Cachucha", 'form':form, 'other':other}
    return render(request, "others/logs/createOther.html", context)


def updateOther(request, pk):
    other = Others.objects.get(id=pk)
    form = OtherForm(instance=other)
    if request.method == 'POST':
        form = OtherForm(request.POST, instance=other)
        if form.is_valid():
            form.save()
            messages.success(request, f'El producto ya quedo guardado!')
            return redirect('home')

    context = {"title":"Modificar Other", 'form':form}
    return render(request, "computo/logs/createOther.html", context)


def delother(request, pk):
    other = Others.objects.get(id=pk)
    other.delete()
    messages.success(request, f'El producto Se elimino!')
    return redirect('home')
