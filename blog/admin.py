from django.contrib import admin

# Register your models here.
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor



class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    #Añadir barra de busqueda, en lista
    search_fields = ['nombre']
    #Colocar los atributos en el encabezado, pasarlo en tupla
    list_display = ('nombre','estado','fecha_creacion',)
    resource_class = CategoriaResource

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombres']
    list_display = ('nombres','correo','estado','fecha_creacion',)
    resource_class = AutorResource

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
