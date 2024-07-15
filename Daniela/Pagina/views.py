from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login,  logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from CarritoApp import models
from Pagina.Form import ProdForm
# Create your views here.
#Crud


def crud(request):
    productos = models.Producto.objects.all()
    context={"productos":productos}
    return render(request, 'listar.html', context)  

@login_required
def agregar(request):
    if request.method == "GET":
        return render(request, 'agregar.html', {"form": ProdForm})
    else:
        try:
            form = ProdForm(request.POST)
            new_Prod = form.save(commit=False)
            new_Prod.user = request.user
            new_Prod.save()
            return redirect('Tienda')
        except ValueError:
            return render(request, 'agregar.html', {"form": ProdForm, "error": "Error al crear producto."})   

def eliminarProd(request):
     productos = models.Producto.objects.get(Producto=models.Producto)
     productos.delete()
     return render(request,'crud.html')

def base(request):
    return render(request, "base.html")
@login_required
def Api(request):
    return render(request, 'Api.html')

def home(request):
    return render(request, 'home.html')

def signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html',{
        'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], 
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')#
            except IntegrityError:
                return render(request, 'signup.html',{
                    'form': UserCreationForm,
                    "error": 'User already exists'
        }) 
    return render(request, 'signup.html',{
        'form': UserCreationForm,
        "error": 'Password do not match'
    })
    

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return  render(request, 'signin.html', {
        'form': AuthenticationForm
    })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
                ['password'])
        if user is None:
            return  render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            }) 
        else:    
            login(request, user)
            return redirect('home')
