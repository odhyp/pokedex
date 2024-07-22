import requests
import os


def fetch_pokemon_data(pokemon_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for Pokémon ID: {pokemon_id}")
        return None


def fetch_pokemon_species_data(pokemon_id):
    url = f'https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}/'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch species data for Pokémon ID: {pokemon_id}")
        return None
