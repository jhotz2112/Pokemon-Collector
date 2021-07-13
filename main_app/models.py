from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    attack = models.TextField(max_length=20)

    def __str__(self):
        return f"{self.name}"
