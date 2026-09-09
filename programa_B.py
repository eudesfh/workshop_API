import random

def dobra_um_numero(num: int):
    return num * 2

def read_numbers_from_file():
    with open("recursos/arquivo.txt", "r") as arquivo:
            last_number = int(arquivo.readlines()[-1])
            return last_number


if __name__ == "__main__":
    last_number = read_numbers_from_file()
    print(last_number)
    doubled_number = dobra_um_numero(last_number)
    print(f"O dobro de {last_number} é {doubled_number}")

