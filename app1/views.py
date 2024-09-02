from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hola, mundo. Esta es la página de inicio de nombreapp.</h1> <br> <p>el titulo tuve que corregirlo yo agregando los <h1> inicial y </h1> final, <br>         atte nelsito</p>")

# Create your views here.
