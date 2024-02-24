def read_file_data(filename):
    with open(filename, "rb") as file:
        return file.read()

def write_file_data(filename, data):
    with open(filename, 'wb') as file:
        file.write(bytes(data))

