
import requests 
from django.core.management.base import BaseCommand
from pokedata.models import Moves

class Command(BaseCommand):
    def handle(self, *args, **options):
        move_id = 1
        max_move_id = 919 
        while move_id <= max_move_id: 
            poke_api_response = requests.get(f"https://pokeapi.co/api/v2/move/{move_id}")
            move_data = poke_api_response.json()
            Moves.objects.get_or_create() 


            move_id += 1 