# Import Api data into database 
# Incorrect so far 
import requests
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    species_id = 1
    while species_id <= 1028:
        poke_api_response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{species_id}/")
        pokemon_data = poke_api_response.json()
        pokemon_name = pokemon_data["name"]
        # print("Pokemon Name: ", pokemon_name)

        species_id +=1
    # limit = 1 
    # poke_url = f"https://pokeapi.co/api/v2/pokemon/?offset=20&limit={limit}"
    # while limit <= 1351: 
        # response = requests.get(poke_url)
        # data = response.json()
        # for pokemon in data["results"]:
            # pokemon_response = requests.get(pokemon["url"])
            # pokemon_data = pokemon_response.json()
            # name = pokemon_data["name"]
            # height = pokemon_data["height"]
            # weight = pokemon_data["weight"]
            # base_experience = pokemon_data["base_experience"]
            # types = [t["type"]["name"] for t in pokemon_data["types"]]
            # abilities = [a["ability"]["name"] for a in pokemon_data["abilities"]]
            # stats = {s["stat"]["name"]: s["base_stat"] for s in pokemon_data["stats"]}
            
            # Save the data to the database
            # from pokedata.models import Pokemon
            # Pokemon.objects.create(
                # name=name,
                # height=height,
                # weight=weight,
                # base_experience=base_experience,
                # types=types,
                # abilities=abilities,
                #stats=stats
            #)
        # limit += 1
        # poke_url = f"https://pokeapi.co/api/v2/pokemon/?offset={limit}&limit={limit}"
        
