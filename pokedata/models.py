from django.db import models

# Create your models here.

class Species(models.Model): 
    name = models.CharField(max_length=100)
    pokedex_id = models.IntegerField(unique=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()
    types = models.JSONField()
    abilities = models.JSONField()
    stats = models.JSONField()
    total_stats = models.IntegerField()
    sprite = models.URLField()
    def __str__(self):
        return self.name
class Moves(models.Model): 
    def __str__(self):
        return self.name