import os
from urllib.parse import urlparse


class LinkParser:
    def __init__(self, input_folder):
        assert os.path.isdir(input_folder), "Input folder does not exist"
        self.input_folder = input_folder

    @staticmethod
    def domain_name(url) -> str:
        return urlparse(url).netloc

    def read_files(self) -> dict[str, set[str]]:
        data_dict = {"text": set()}

        for file in os.listdir(self.input_folder):
            file = os.path.join(self.input_folder, file)

            if os.path.isdir(file):  # ignore folders
                continue

            with open(file, "r", encoding="utf-8") as read_file:
                for line in read_file:
                    line = line.strip()

                    if "http" not in line or "https" not in line:  # check link or text
                        if line != "":
                            data_dict["text"].add(line)
                        continue

                    domain = self.domain_name(line)

                    if domain in data_dict:
                        data_dict[domain].add(f"{line}")
                    else:
                        data_dict[domain] = set()
                        data_dict[domain].add(f"{line}")

        return data_dict


class DataOutput:
    def __init__(self, output_folder, output_file_name):
        assert len(output_file_name) > 0, "Filename for output file must be provided"
        assert os.path.isdir(output_folder), "Output folder does not exist"
        self.output_path = output_folder + "/" + output_file_name

    def generate_text_file(self, data) -> None:
        with open(self.output_path + ".txt", "w", encoding="utf-8") as write_file:
            for key, value in data.items():
                write_file.write(f"[---{key}---]\n")
                for item in value:
                    write_file.write(f"{item}\n")
                write_file.write("\n")
        print(f"Output TEXT file: {self.output_path} was created")
