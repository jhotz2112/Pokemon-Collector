from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Pokemon
from .forms import EvolutionForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
  pokemon = Pokemon.objects.all()
  return render(request, 'pokemon/index.html', { 'pokemon': pokemon })

def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  evolution_form = EvolutionForm()
  return render(request, 'pokemon/detail.html', {
    'pokemon': pokemon,
    'evolution_form': evolution_form,
  })

class PokemonCreate(CreateView):
  model = Pokemon
  fields = '__all__'

class PokemonUpdate(UpdateView):
  model = Pokemon
  fields = ['name', 'type', 'description', 'weakness']

class PokemonDelete(DeleteView):
  model = Pokemon
  success_url = '/pokemon/'

def add_evolution(request, pokemon_id):
  form = EvolutionForm(request.POST)
  if form.is_valid():
    new_evolution = form.save(commit=False)
    new_evolution.pokemon_id = pokemon_id
    new_evolution.save()
  return redirect('detail', pokemon_id=pokemon_id)