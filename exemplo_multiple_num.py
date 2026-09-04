import time

def dobra_um_numero(num):
    return num * 2

def ler_ultimo_numero():
    try:
        with open('numeros.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            if linhas:
                ultimo_numero = int(linhas[-1].strip())
                return ultimo_numero
            else:
                print("Arquivo está vazio.")
                return None
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    while True:
        ultimo_numero = ler_ultimo_numero()
        if ultimo_numero is not None:
            resultado = dobra_um_numero(ultimo_numero)
            print(f"O dobro de {ultimo_numero} é {resultado}")
        time.sleep(1)