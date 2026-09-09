import random

def numero_aleatorio():
    return random.randint(1, 95)

def dobra_um_numero(num: int):
    return num * 2

def main():
    num = numero_aleatorio()
    num_dobrado = dobra_um_numero(num)
    print(f"O dobro de {num} é {num_dobrado}")

if __name__ == "__main__":
    main()

    