from django.db import models

# Create your models here.

class Species(models.Model): 
    name = models.CharField(max_length=100)
    id = models.IntegerField()
    # height = models.IntegerField()
    # weight = models.IntegerField()
    # base_experience = models.IntegerField()
    types = models.JSONField()
    abilities = models.JSONField()
    stats = models.JSONField()
    sprite = models.URLField()
class Todo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)