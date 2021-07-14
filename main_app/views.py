from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Pokemon

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Gotta Catch 'Em All<h1>")

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
  pokemon = Pokemon.objects.all()
  return render(request, 'pokemon/index.html', { 'pokemon': pokemon })

def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  return render(request, 'pokemon/detail.html', { 'pokemon': pokemon })

class PokemonCreate(CreateView):
  model = Pokemon
  fields = '__all__'

class PokemonUpdate(UpdateView):
  model = Pokemon
  fields = ['name', 'type', 'description', 'weakness']

class PokemonDelete(DeleteView):
  model = Pokemon
  success_url = '/pokemon/'