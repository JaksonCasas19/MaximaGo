from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name='index'),
    path('generales/',generales,name='generales'),
    path('turismo/',turismo,name='turismo'),
    path('tecnologia/',tecnologia,name='tecnologia'),
    path('noticia/',noticia,name='noticia'),
    path('<slug:slug>/',detallePost, name='detalle_post'),
]
