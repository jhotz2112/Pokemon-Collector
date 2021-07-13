from django.shortcuts import render
from .models import Pokemon

class Pokemon:  # Note that parens are optional if not inheriting from another class
  def __init__(pkmn, name, type, description, attack):
    pkmn.name = name
    pkmn.type = type
    pkmn.description = description
    pkmn.attack = attack

pokemon = [
  Pokemon('Lolo', 'tabby', 'foul little demon', 3),
  Pokemon('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Pokemon('Raven', 'black tripod', '3 legged cat', 4)
]

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Gotta Catch 'Em All<h1>")

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    return render(request, 'pokemon/index.html', { 'pokemon': pokemon })
