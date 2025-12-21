from django.shortcuts import render

def home(request):
    return render(request, 'mainapp/home.html')

def colleges(request):
    return render(request, 'mainapp/colleges.html')

def svecw1(request):
    return render(request, 'mainapp/svecw1.html')

def vit(request):
    return render(request, 'mainapp/vit.html')

def bvrit(request):
    return render(request, 'mainapp/bvrit.html')


