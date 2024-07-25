import os
import shutil

from src.data_fetcher import DataFetcher
from src.generate_content import GenerateContent


NUMBER_OF_POKEMON = 6


def load_data(number_of_pokemon):
    for i in range(number_of_pokemon):
        i += 1

        # Fetching base data and species data
        data_fetcher = DataFetcher()
        base_data = data_fetcher.fetch_pokemon_data(pokemon_id=i)
        species_data = data_fetcher.fetch_pokemon_species_data(pokemon_id=i)

        # Generates markdown
        generator = GenerateContent()
        generator.generate_markdown(file_name=str(i).zfill(3),
                                    base_data=base_data,
                                    species_data=species_data)


def clear_content():
    try:
        dir_path = 'content/pokemon/'
        shutil.rmtree(dir_path)
        os.mkdir(dir_path)
    except Exception as e:
        raise e


def main():
    # clear_content()
    load_data(NUMBER_OF_POKEMON)


if __name__ == '__main__':
    main()
