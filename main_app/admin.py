from django.contrib import admin

from .models import Pokemon, Evolution

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Evolution)