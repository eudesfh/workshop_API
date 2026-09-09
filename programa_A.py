import random
import time

def numero_aleatorio():
    num = random.randint(1, 95)
    with open("recursos/arquivo.txt", "a") as arquivo:
        arquivo.write(f"{num}\n")


if __name__ == "__main__":
    while True:
        numero_aleatorio()
        time.sleep(1)  # Aguarda 1 segundo antes de gerar o próximo número