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
    name = models.CharField(max_length=100)
    move_id = models.IntegerField(unique = True)
    power = models.IntegerField(null=True)
    accuracy = models.IntegerField(null=True)
    effect_chance = models.IntegerField(null=True)
    pp = models.IntegerField()
    meta = models.JSONField()
    stat_changes = models.JSONField(null=True)
    # Meta refers to the metadata of the move, so attributes like move effect such as "has a 30% chance to paralyze the target"
    #  or "increases the user's speed by 1 stage" would be stored in this field.
    priority = models.IntegerField()
    type = models.CharField(max_length=100)
    damage_class = models.CharField(max_length=100)
    def __str__(self):
        return self.name