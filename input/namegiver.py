import os

def get_file_names_in_directory():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_names = [f for f in os.listdir(script_directory) if os.path.isfile(os.path.join(script_directory, f))]
    return file_names

print(get_file_names_in_directory())