import os

script_directory = os.path.dirname(os.path.abspath(__file__))

def read_data(file_dir: str, file_name: str) -> str:
    file_path = os.path.join(script_directory, '..', file_dir, file_name)
    data = None
    with open(file_path, 'r') as file:
        data = file.read()
    return data