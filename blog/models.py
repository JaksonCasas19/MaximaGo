from django.db import models
from django.db.models.base import Model

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la Categoria',max_length=50,null=False,blank=False)
    estado = models.BooleanField('Categoria Activada/Categoria no Activada', default=True)
    fecha_creacion = models.DateField("Fecha de creacion",auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombre de Autor', max_length=50,null=False,blank=False)
    apellidos= models.CharField('Apellidos de autor',max_length=50,null=False,blank=False)
    twitter = models.URLField('Twitter',null=True,blank=True)
    web = models.URLField('Web',null=True,blank=True)
    correo = models.EmailField('Correo electronico',null=False,blank=False)
    estado = models.BooleanField('Autor Activo/No Activo',default=True)
    fecha_creacion = models.DateField("Fecha de creacion",auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0},{1}".format(self.nombres, self.apellidos)