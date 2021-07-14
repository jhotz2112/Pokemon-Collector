from django.db import models
from django.urls import reverse

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    weakness = models.TextField(max_length=100)

    def __str__(pkmn):
        return f"{pkmn.name} is described as {pkmn.description} and is a {pkmn.type} type pokemon"

    def get_absolute_url(pkmn):
        return reverse('detail', kwargs={'pokemon_id': pkmn.id })