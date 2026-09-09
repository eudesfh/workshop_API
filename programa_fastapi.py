from fastapi import FastAPI
import random
import time

servidor = FastAPI()

@servidor.get("/recursos")

def numero_aleatorio():
    num = random.randint(1, 95)
    print(num)
    return num

