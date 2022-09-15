from django.shortcuts import render


def home(request):


    context = {"title": "Home"}
    return render(request, "allPcs/home.html", context)
