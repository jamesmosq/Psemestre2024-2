#Remover elementos de una lista mientras cumplen una condición
numeros = [2, 4, 6, 7, 8, 10, 11, 12]
while numeros and numeros[0] % 2 == 0:
    numeros.pop(0)

print("Lista después de remover pares del inicio:", numeros)