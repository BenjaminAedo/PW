from django.shortcuts import render, redirect
from CarritoApp.models import Producto
from CarritoApp.Carrito import Carrito
from django.contrib.auth.decorators import login_required

# Create your views here.


# Carrito
@login_required
def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos': productos})

@login_required
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

@login_required
def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

@login_required
def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

@login_required
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")
