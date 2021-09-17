from blog.models import Post
from django.shortcuts import render
from .models import Categoria, Post
# Create your views here.

def home(request):
    posts = Post.objects.filter(estado=True)
    return render(request,'index.html',{'posts':posts})

def generales(request):
    return render(request,'generales.html')

def turismo(request):
    posts = Post.objects.filter(estado=True,categoria= Categoria.objects.get(nombre='Turismo'))
    
    return render(request,'turismo.html',{'posts':posts})

def tecnologia(request):
    posts = Post.objects.filter(estado=True,categoria= Categoria.objects.get(nombre='Tecnologia'))
    return render(request,'tecnologia.html',{'posts':posts})

def noticia(request):
    return render(request,'noticia.html')