# Import Api data into database 

import requests
from django.core.management.base import BaseCommand
from pokedata.models import Species 

class Command(BaseCommand):
    def handle (self, *args, **options):
        species_id = 1
        max_species_id = 1025
        while species_id <= max_species_id:
            poke_api_response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{species_id}/")
            pokemon_data = poke_api_response.json()
            Species.objects.get_or_create(
                pokedex_id = pokemon_data["id"], 
                defaults= { 
                    "name" : pokemon_data["name"],
                    "types" : pokemon_data["types"],
                    "height" : pokemon_data["height"],
                    "weight" : pokemon_data["weight"],
                    "base_experience" : pokemon_data["base_experience"],
                    "abilities" : pokemon_data["abilities"],
                    "stats" : pokemon_data["stats"],
                    "sprite" : pokemon_data["sprites"]["other"]["official-artwork"]["front_default"],
                },
            )
            
            species_id +=1
        
