#!/usr/bin/env python
import getopt
import sys

from link_sorter.LinkParser import LinkParser, DataOutput

input_folder: str = "input_folder"
output_folder: str = "output_folder"
output_file_name: str = "result"

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:f:")
    except getopt.GetoptError:
        print("main.py -i <input_folder> -o <output_folder> -f <output_file_name>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print("main.py -i <input_folder> -o <output_folder> -f <output_file_name>")
            sys.exit()
        elif opt in ("-i", "--input_folder"):
            input_folder = arg
        elif opt in ("-o", "--output_folder"):
            output_folder = arg
        elif opt in ("-f", "--output_file_name"):
            output_file_name = arg

    link_parser = LinkParser(input_folder)
    data_output = DataOutput(output_folder, output_file_name)
    data = link_parser.read_files()
    data_output.generate_header_text_file(data)
