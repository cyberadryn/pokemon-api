import os
import requests
import io
from imgcat import imgcat
from PIL import Image
from io import BytesIO

# Base Url
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
   
    if response.status_code == 200:
        pokemon_data = response.json()
        return(pokemon_data)
    else:
        print(f"Failed to retrieve date {response.status_code}")

# Prompt for Pokemon Name
pokemon_name = input("Enter Pokemon name: ").lower()
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
   print("\n")

   # Pokemon Image
   response = requests.get(pokemon_info["sprites"]["front_default"])
   img = Image.open(BytesIO(response.content))
   imgcat(img)

   # Pokemon Info
   print ("Name: " + f"{pokemon_info["name"].capitalize()}")
   print ("ID: "f"{pokemon_info["id"]}")
   print ("Height: " f"{pokemon_info["height"]}") 
   print ("Weight: " f"{pokemon_info["weight"]}") 
   print(f"Types: {', '.join([q['type']['name'].capitalize() for q in pokemon_info['types']])}")
   print(f"Abilities: {', '.join([g['ability']['name'].capitalize() for g in pokemon_info['abilities']])} \n")
   print(f"Learnable Moves: {', '.join([bs['move']['name'].capitalize() for bs in pokemon_info['moves']])}")
   
 