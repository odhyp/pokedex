from mdutils.mdutils import MdUtils


OUTPUT_PATH = "content/pokemon/"


class GenerateContent:
    def get_pokemon_type(self, types_list):
        if len(types_list) == 2:
            return [types_list[0]["type"]["name"], types_list[1]["type"]["name"]]
        elif len(types_list) == 1:
            return [types_list[0]["type"]["name"]]
        else:
            return None

    def generate_markdown(self, file_name, base_data, species_data):
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
