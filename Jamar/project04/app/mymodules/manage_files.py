import shutil
import os
import json


def export_string_to_txt(string_to_export, filename):
    try:
        with open(filename, 'w') as file:
            file.write(string_to_export)
        print("String successfully exported to", filename)
    except IOError:
        print("Error: Unable to write to file", filename)

def delete_contents_of_folder(folder_path):
    # Iterate over all the files and subdirectories in the folder
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in files:
            # Delete each file
            file_path = os.path.join(root, name)
            os.remove(file_path)
        for name in dirs:
            # Delete each subdirectory
            dir_path = os.path.join(root, name)
            shutil.rmtree(dir_path)

def delete_folder(folder_path):
    try:
        # Delete the folder and its contents
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting folder '{folder_path}': {e}")


def json_touch(string_data):
    # Given string containing dictionary within a dictionary
    # string_data = "{'json': '\nSystem: {'Raiz cuadrada': 2, 'Raiz cubica': 1.5874010519681994, 'Division por 10': 0.4}'}"

    print('\n-----------------------------------------------')
    print(string_data)
    print('---')
    # Extracting the dictionary-like string from the value of the 'json' key
    start_index = string_data.find("{")
    end_index = string_data.rfind("}") + 1
    inner_string = string_data[start_index:end_index]

    # Removing '\n' characters from the inner string
    inner_string = inner_string.replace('\n', '')

    # Convert the inner string to dictionary
    inner_dict = eval(inner_string)

    # Convert the extracted dictionary to JSON
    json_data = json.dumps(inner_dict)

    return json_data