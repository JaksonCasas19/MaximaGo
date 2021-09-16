from django.contrib import admin

# Register your models here.
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
    #Añadir barra de busqueda
    search_fields = ['nombre']


admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor)