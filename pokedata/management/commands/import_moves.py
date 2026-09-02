
import requests 
from django.core.management.base import BaseCommand
from pokedata.models import Moves

class Command(BaseCommand):
    def handle(self, *args, **options):
        move_id = 1
        max_move_id = 919 
        while move_id <= max_move_id: 
            poke_api_response = requests.get(f"https://pokeapi.co/api/v2/move/{move_id}/")
            move_data = poke_api_response.json()
            damage_class = move_data["damage_class"]["name"]
            type = move_data["type"]["name"]
            # Make field into a tuple using this: "ailment": move_data["meta"]["ailment"]
            meta = move_data["meta"]["ailment"]["name"] if move_data["meta"]["ailment"] else None, 
            move_data["meta"]["category"]["name"], 
            move_data["meta"]["min_hits"], move_data["meta"]["max_hits"], move_data["meta"]["min_turns"], move_data["meta"]["max_turns"], 
            move_data["meta"]["drain"], move_data["meta"]["healing"], move_data["meta"]["crit_rate"], move_data["meta"]["ailment_chance"], 
            move_data["meta"]["flinch_chance"], move_data["meta"]["stat_chance"]
            Moves.objects.get_or_create(
                move_id = move_data["id"], 
                defaults = { 
                    "name" : move_data["name"], 
                    "power": move_data["power"], 
                    "accuracy" : move_data["accuracy"],
                    "priority": move_data["priority"],
                    "pp" : move_data["pp"],
                    "effect_chance": move_data["effect_chance"],
                    "damage_class" : damage_class, 
                    "type" : type, 
                    "meta" : meta
                }
            ) 


            move_id += 1 
