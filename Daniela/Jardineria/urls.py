"""
URL configuration for Jardineria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from CarritoApp.views import agregar_producto, eliminar_producto, limpiar_carrito, restar_producto, tienda
from Pagina import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('Api/', views.Api, name='Api'),
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    #Crud
    path('crud/', views.crud, name='crud'),
    path('eliminarProd/', views.eliminarProd, name='eliminarProd'),
    path('agregar/', views.agregar, name='agregar'),
    
    #CarritoApp
    path('tienda/', tienda, name='Tienda'),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    
]
