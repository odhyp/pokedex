from mdutils.mdutils import MdUtils


OUTPUT_PATH = "content/pokemon/"


class GenerateContent:
    def generate_markdown(self, file_name, base_data, species_data):
        output_path = f"{OUTPUT_PATH}{file_name}"
        md = MdUtils(file_name=output_path)

        # Front Matter
        md.new_paragraph('+++')
        md.new_paragraph(f'ID = "{str(base_data["id"]).zfill(3)}"')
        md.new_paragraph(f'Name = "{base_data["name"]}"')
        md.new_paragraph(f'Sprites = "{base_data["sprites"]["front_default"]}"')

        type1 = base_data["types"][0]["type"]["name"]
        type2 = base_data["types"][1]["type"]["name"]

        md.new_paragraph(f'Types = ["{type1}", "{type2}"]')
        md.new_paragraph('+++')
        md.new_paragraph('')

        # Page Content here

        md.create_md_file()
