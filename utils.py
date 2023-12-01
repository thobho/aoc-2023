def read_data(file_name: str) -> str:
    data = None
    with open(file_name, 'r') as file:
        data = file.read()
    return data