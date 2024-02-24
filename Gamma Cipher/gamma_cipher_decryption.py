from file_handling_functions import read_file_data as rf
from file_handling_functions import write_file_data as wf


def decrypt(filename, key):
    file_data = rf(filename)
    decrypted_data = []
    print("Длина ключа =", len(key))
    print("Длина даты =", len(file_data))
    if len(key) < len(file_data):
        while len(key) < len(file_data):
            key.extend(key * (((len(file_data) - len(key)) + len(key) - 1) // len(key)))
            print("Длина ключа =", len(key))
    print("Длина ключа =", len(key))
    print("Длина даты =", len(file_data))
    decrypted_data = (p ^ y for p, y in zip(file_data, key))
    wf(filename, decrypted_data)

key = [1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1]
filename = r""
decrypt(filename, key)