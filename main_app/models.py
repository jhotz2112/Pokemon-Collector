from django.db import models
from django.urls import reverse
from datetime import date

EVOLUTION = (
    ('1st', 'First Evolution'),
    ('2nd', 'Second Evolution'),
    ('3rd', 'Mega Evolution')
 )


class Attack(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=70)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('attacks_detail', kwargs={'pk': self.id})


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    weakness = models.TextField(max_length=100)
    attacks = models.ManyToManyField(Attack)

    def __str__(self):
        return f"{self.name} is described as {self.description} and is a {self.type} type pokemon"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id })

    def evolution_for_today(self):
        return self.evolution_set.filter(date=date.today()).count() >= len(EVOLUTION)  

class Evolution(models.Model):
    date = models.DateField('Date Evolved')
    evolution = models.CharField(
        'Evolution Time',
        max_length=3,
        choices=EVOLUTION,
        default=EVOLUTION[0][0]
    )

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_evolution_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

