import os

input_folder: str = "input_folder"
output_file_name: str = ""


def domain_name(url) -> str:
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


def dict_create(file) -> dict:
    data_dict = {'text': []}
    for file in os.listdir(file):
        file = input_folder + '/' + file
        if os.path.isdir(file):  # ignore folders
            continue

        with open(file, 'r') as f:
            for line in f:
                line = line.strip()
                if line == '':
                    continue

                if 'http://' or 'https://' not in line:  # check link or text
                    data_dict['text'].append(line)
                    continue

                domain = domain_name(line)
                if domain in data_dict:
                    data_dict[domain].append(line)

                else:
                    data_dict[domain] = [line]
    return data_dict


def file_write(data, file_name) -> None:
    with open(file_name, 'w') as f:

        for key, value in data.items():
            f.write(f"[---{key}---]\n")
            for item in value:
                f.write(f"{item}\n")


def error_check(folder, file) -> bool:
    if not os.path.isdir(folder):
        return True, f"Folder \"{input_folder}\" does not exist"

    if len(file) == 0:
        return True, f"Filename must be provided"

    return False, None


if __name__ == '__main__':
    error, message = error_check(input_folder, output_file_name)
    if error:
        print(message)
    else:
        processed_dict = dict_create(input_folder)

        file_write(processed_dict, output_file_name)
