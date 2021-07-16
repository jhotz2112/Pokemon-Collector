from django.forms import ModelForm
from .models import Evolution

class EvolutionForm(ModelForm):
  class Meta:
    model = Evolution
    fields = ['date', 'evolution']