from blog.models import Post
from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    posts = Post.objects.filter(estado=True)
    return render(request,'index.html',{'posts':posts})

def generales(request):
    return render(request,'generales.html')

def turismo(request):
    return render(request,'turismo.html')

def tecnologia(request):
    return render(request,'tecnologia.html')

def noticia(request):
    return render(request,'noticia.html')