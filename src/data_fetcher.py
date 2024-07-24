import requests


class DataFetcher:
    """
    A class to fetch data related to Pokémon from the PokéAPI.
    """

    def fetch_pokemon_data(self, pokemon_id: int) -> dict:
        """
        Fetches data for a specific Pokémon by ID.

        Args:
            pokemon_id (int): The ID of the Pokémon.

        Returns:
            dict: The JSON data of the Pokémon if the request is successful.
            None: If the request fails.
        """
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data for Pokémon ID: {pokemon_id}")
            return None

    def fetch_pokemon_species_data(self, pokemon_id: int) -> dict:
        """
        Fetches species data for a specific Pokémon by ID.

        Args:
            pokemon_id (int): The ID of the Pokémon species.

        Returns:
            dict: The JSON data of the Pokémon species if the request is successful.
            None: If the request fails.
        """
        url = f'https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}/'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch species data for Pokémon ID: {pokemon_id}")
            return None
