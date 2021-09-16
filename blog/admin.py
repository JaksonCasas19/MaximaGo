from django.contrib import admin

# Register your models here.
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
    #Añadir barra de busqueda, en lista
    search_fields = ['nombre']
    #Colocar los atributos en el encabezado, pasarlo en tupla
    list_display = ('nombre','estado','fecha_creacion',)

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombres']
    list_display = ('nombres','correo','estado','fecha_creacion',)

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)