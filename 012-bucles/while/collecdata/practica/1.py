# Procesar una lista hasta encontrar un valor específico
numeros = [1, 3, 5, 7, 9, 11, 13, 15]
objetivo = 11
indice = 0

while indice < len(numeros):
    if numeros[indice] == objetivo:
        print(f"Encontrado {objetivo} en el índice {indice}")
        break
    indice += 1
else:
    print(f"{objetivo} no encontrado en la lista")

