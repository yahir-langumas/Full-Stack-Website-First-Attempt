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
    
class Todo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)