from mdutils.mdutils import MdUtils


OUTPUT_PATH = "content/pokemon/"


class GenerateContent:
    """
    A class to generate markdown content for Pokémon data.
    """

    def get_pokemon_type(self, types_list: list):
        """
        Retrieves the types of a Pokémon from the provided list.

        Args:
            types_list (list): A list of dictionaries containing type information.

        Returns:
            list: A list of type names. If there are two types, both are returned. If there is one type, only that type is returned.
            None: If the list is empty.
        """
        if len(types_list) == 2:
            return [types_list[0]["type"]["name"], types_list[1]["type"]["name"]]
        elif len(types_list) == 1:
            return [types_list[0]["type"]["name"]]
        else:
            return None

    def generate_markdown(self,
                          file_name: str,
                          base_data: dict,
                          species_data: dict):
        """
        Generates a markdown file for a Pokémon with the provided data.

        Args:
            file_name (str): The name of the markdown file to be created.
            base_data (dict): The base data of the Pokémon.
            species_data (dict): The species data of the Pokémon.
        """
        output_path = f"{OUTPUT_PATH}{file_name}"
        md = MdUtils(file_name=output_path)

        # Front Matter
        md.new_paragraph('+++')
        md.new_paragraph(f'ID = "{str(base_data["id"]).zfill(3)}"')
        md.new_paragraph(f'Name = "{base_data["name"]}"')
        md.new_paragraph(f'Sprites = "{base_data["sprites"]["front_default"]}"')

        types = self.get_pokemon_type(base_data["types"])

        md.new_paragraph(f'Types = {types}')
        md.new_paragraph('+++')
        md.new_paragraph('')

        # Page Content here

        md.create_md_file()
