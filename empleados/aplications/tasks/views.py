from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

from django.views.generic.list import  ListView
from .models import Menu,Categoria,Productos
from django.contrib import messages


# Create your views here.
def home(request):
    template_name="tasks/home.html"
    categorias = Categoria.objects.filter(activo=True)
    productos = Productos.objects.filter(activo=True)
    context = {"productos": productos, "categorias": categorias}
    return render(request,template_name,context)






def buscar_categorias(request,slug):
    template_name="tasks/Tasks.html"
    cat=Categoria.objects.get(slug=slug)
    categorias=Categoria.objects.filter(activo=True)
    productos=Productos.objects.filter(activo=True,categoria=cat)
    context = {"productos":productos,"categorias":categorias}
    return render(request,template_name,context)

def search(request):
    template_name="tasks/Tasks.html"
    q=request.GET["q"]
    productos=Productos.objects.filter(activo=True,nombre__icontains=q)
    categorias=Categoria.objects.filter(activo=True)
    context = {"productos":productos,"categorias":categorias}
    return render(request,template_name,context)

def detail(request,slug):
    if Productos.objects.filter(activo=True, slug=slug).exists():
        template_name = 'tasks/home.html'
        producto=Productos.objects.get(activo=True,slug=slug)
        categorias=Categoria,objects.filter(axtivo=True)
        context = {"producto":productos,"categorias":categorias}
        return render(request,template_name,context)


def cart(request,slug):
    product= Productos.objects.get(slug=slug)

    initial = {"items":[],"price":0.0,"count":0}
    session=request.session.get("data", initial)
    if slug in session["items"]:
        messages.error(request,"Productos ya existe en el Carrito")
    else:
        session["items"].append(slug)
        session["price"] += float(product.precio)
        session["count"] +=1
        request.session["data"]=session
        messages.success(request,"Agregado Exitosamente")
    return redirect("tasks:detail", slug)    

def mycart(request):
    template_name = "tasks/mycart.html"
    session = request.session.get("data", {"items": []})
    productos = Productos.objects.filter(slug__in=sess["items"], activo=True)
    categorias = Categoria.objects.filter(activo=True)
    context = {"productos": productos, "categorias": categorias}
    return render(request, template_name, context)




def signup(request):
    if request.method == 'GET':
        return render(request, 'tasks/signup.html',{
            'form':UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST
                    ['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'tasks/signup.html', {
                    'form': UserCreationForm,
                    "error": 'User alredy exist'
                })
        return render(request, 'tasks/signup.html', {
                'form': UserCreationForm,
                "error": 'Password do not match'
        })
    
def tasks(request):
    return render(request, 'tasks/Tasks.html')

    

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'tasks/signin.html', {
        'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'tasks/signin.html', {
                'form': AuthenticationForm,
                "error": 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('home')

        

class MenuView(ListView):
    model = Menu
    template_name = 'tasks/Tasks.html'
    context_object_name = 'lista_prueba'    

