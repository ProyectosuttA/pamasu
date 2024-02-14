"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from administrador import views
#from plataforma import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="inicio"),
#    path('registro/',views.registro, name="registro" ),
    path('plataforma/',views.plataforma, name="plataforma" ),
#   path('administrador/',views.administrador, name="administrador"),
    path('salir/',views.salir, name="salir"),
    path('registrar/',views.registrar, name="registrar"),
    path('consultar/',views.consultar, name="consultar"),
    path('seguimiento/',views.seguimiento, name="seguimiento"),
    path('comentarios/',views.comentarios, name="comentarios"),
    path('comentario/',views.comentario, name="comentario"),
    path('ingresar/',views.ingresar, name="ingresar")
    

 #   path('inicio/',views.inicio)
]
