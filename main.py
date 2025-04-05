from link_sorter.LinkParser import LinkParser, DataOutput

input_folder: str = "input_folder"
output_folder: str = "output_folder"
output_file_name: str = "test"

if __name__ == "__main__":
    link_parser = LinkParser(input_folder)
    data_output = DataOutput(output_folder, output_file_name)
    data = link_parser.read_files()
    data_output.generate_text_file(data)
