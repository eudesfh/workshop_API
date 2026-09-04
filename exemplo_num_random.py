import time
import random


def gerar_numero_aleatorio():
    num = random.randint(1, 100)
    print(num)
    with open('numeros.txt', 'a') as arquivo:
        arquivo.write(f"{num}\n")

if __name__ == "__main__":
    while True:
        gerar_numero_aleatorio()
        time.sleep(1)