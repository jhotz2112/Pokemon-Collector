from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('pokemon/', views.pokemon_index, name='index'),
    path('pokemon/<int:pokemon_id>/', views.pokemon_detail, name='detail'),
    path('pokemon/create/', views.PokemonCreate.as_view(), name='pokemon_create'),
    path('pokemon/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemon_update'),
    path('pokemon/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemon_delete'),
    path('pokemon/<int:pokemon_id>/add_evolution/', views.add_evolution, name='add_evolution'),
    path('pokemon/<int:pokemon_id>/assoc_attack/<int:attack_id>/', views.assoc_attack, name='assoc_attack'),
    path('pokemon/<int:pokemon_id>/unassoc_attack/<int:attack_id>/', views.unassoc_attack, name='unassoc_attack'),
    path('attacks/', views.AttackList.as_view(), name='attacks_index'),
    path('attacks/<int:pk>/', views.AttackDetail.as_view(), name='attacks_detail'),
    path('attacks/create/', views.AttackCreate.as_view(), name='attacks_create'),
    path('attacks/<int:pk>/update/', views.AttackUpdate.as_view(), name='attacks_update'),
    path('attacks/<int:pk>/delete/', views.AttackDelete.as_view(), name='attacks_delete'),
]