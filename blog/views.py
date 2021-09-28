from blog.models import Post
from django.shortcuts import render
from .models import Categoria, Post
from django.db.models import Q
# Create your views here.

def home(request):
    #print(request.GET) /Para capturar en el buscador
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado=True)

    #Verificar si el texto pasado en el buscador existe
    if queryset:
        posts = Post.objects.filter(
            Q(titulo = queryset) |
            Q(descripcion = queryset)
        ).distinct
    
    return render(request,'index.html',{'posts':posts})

def detallePost(request,slug):
    post = Post.objects.get(
        slug = slug
    )
    print(post)
    return render(request,'post.html',{'detalle_post':post})

def generales(request):
    posts = Post.objects.filter(estado=True,categoria= Categoria.objects.get(nombre__iexact='General')) #Nombre__iexat Mayus y Minus
    return render(request,'generales.html',{'posts':posts})

def turismo(request):
    posts = Post.objects.filter(estado=True,categoria= Categoria.objects.get(nombre='Turismo'))
    return render(request,'turismo.html',{'posts':posts})

def tecnologia(request):
    posts = Post.objects.filter(estado=True,categoria= Categoria.objects.get(nombre='Tecnologia'))
    return render(request,'tecnologia.html',{'posts':posts})

def noticia(request):
    posts = Post.objects.filter(estado=True,categoria= Categoria.objects.get(nombre='Noticia'))
    return render(request,'noticia.html',{'posts':posts})