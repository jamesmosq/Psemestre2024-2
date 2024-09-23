#Llenar una lista con elementos aleatorios:

import random

lista_aleatoria = []
longitud_deseada = 10

while len(lista_aleatoria) < longitud_deseada:
    elemento = random.randint(1, 100)
    lista_aleatoria.append(elemento)

print("Lista de números aleatorios:", lista_aleatoria)