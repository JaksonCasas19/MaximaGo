from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def generales(request):
    return render(request,'generales.html')

def turismo(request):
    return render(request,'turismo.html')

def tecnologia(request):
    return render(request,'tecnologia.html')

def noticia(request):
    return render(request,'noticia.html')